
from openai import OpenAI

# Your API key (please use environment variable in production)
API_KEY = "Write_your_API_Key"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)
chat = []

while True:

    text = input("User: ")

    if text.lower() == "exit":
        print("Chat ended.")
        break

    ro = {
        "role": "user",
        "content": text
    }

    chat.append(ro)

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        messages=chat
    )

    if response.choices is None or len(response.choices) == 0:
        print("No response received.")
        print(response)
        continue

    airesponse = response.choices[0].message.content

    airo = {
        "role": "assistant",
        "content": airesponse
    }

    chat.append(airo)

    print("AI:", airesponse)