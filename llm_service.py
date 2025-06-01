import os
# to import environment variables
import requests
#let you make web request like sending data to API

# Load your DeepSeek API key directly from environment variables
API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"

# Define a function to ask the DeepSeek LLM take i/p as strign and give output as string
def ask_llm(question: str) -> str:
    # Set request headers
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Set the message to send to DeepSeek
    body = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    # Send the request to DeepSeek
    response = requests.post(API_URL, headers=headers, json=body)

    # Return the result if successful
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error {response.status_code}: {response.text}"
