from llama_index.core import Document
from llama_index.core.readers.base import BaseReader
from typing import List
import requests
from bs4 import BeautifulSoup

class CustomWebPageReader(BaseReader):
    def __init__(self, url):
        self.url = url
        
    def load_data(self) -> List[Document]:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Try multiple selectors to find main content
            content_selectors = [
                "div.main-content",
                "main",
                "article",
                "div.content",
                "div.documentation",
                "div.docs-content",
                "[role='main']",
                "div.markdown-body",
                "div.page-content"
            ]
            
            main_content = None
            for selector in content_selectors:
                main_content = soup.select_one(selector)
                if main_content:
                    break
            
            # If no specific content area found, get body content but exclude navigation
            if not main_content:
                # Remove common navigation elements
                for nav_elem in soup.select("nav, header, footer, .sidebar, .navigation, .menu"):
                    nav_elem.decompose()
                
                main_content = soup.find("body")
            
            if main_content:
                text = main_content.get_text(separator="\n", strip=True)
                # Clean up excessive whitespace
                lines = [line.strip() for line in text.split('\n') if line.strip()]
                clean_text = '\n'.join(lines)
                return [Document(text=clean_text, metadata={"url": self.url})]
            else:
                return [Document(text="No content found on the page.", metadata={"url": self.url})]

        except requests.exceptions.RequestException as e:
            return [Document(text=f"Error fetching URL: {e}", metadata={"url": self.url})]
        
        
web_reader = CustomWebPageReader(url="https://docs.llamaindex.ai/en/stable/examples/llm/groq/")
documents = web_reader.load_data()
print(documents[0].text)