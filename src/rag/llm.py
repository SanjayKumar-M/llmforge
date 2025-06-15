from groq import Groq
from dotenv import load_dotenv
load_dotenv()


def get_response(query,chunks):
    prompt = f"You are an expert Resume reviewer having deep expertise in reviewing the resume and giving constructive feedback based on the requirement. The feedback should be detailed and end with final verdict whether the candidate will be a perfect one for the role or not. Here is the user query and the resume details {query} {chunks}"
    client = Groq()
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_completion_tokens=1024,
        top_p=0.8,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message
