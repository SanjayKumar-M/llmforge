with open("../data/data.txt", "r", encoding="utf-8") as file:  # extracting the data from the file
    data = file.read()
        

# manual extraction or preprocessing textual data for NLP i.e tokenization
import re
result = re.split(r'([,.:;?!]|\s)', data)  # pattern to split by spaces, commas and other marks and words
result = [item.strip() for item in result if item.strip()]  # removing empty strings and stripping whitespace
print(len(result))
all_words = sorted(set(result))  # sorting the unique words
print(len(all_words))  # printing the number of unique words




 