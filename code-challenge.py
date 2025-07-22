import requests
import json

with open('context.json') as f:
    context = json.load(f)


query = input("Enter your query: ")


prompt = f"""
Given the following data:

{context}

Please code the following based on the data provided:
{query}
"""

print(prompt)

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "llama3.2",
        "messages": [
            {"role": "system", "content": "You are a code generator AI. You will generate HTML code that complies with the user's request."},
            {"role": "user", "content": prompt}
        ]
    }
)


message = ""
if response.status_code == 200:
    for line in response.text.splitlines():
        text = json.loads(line)
        text = text['message']['content']
        if text:
            message += text

    print("Response from the model:")
    print(message)
else:
    print(f"Error: {response.status_code} - {response.text}")
