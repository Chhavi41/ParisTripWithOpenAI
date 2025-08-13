import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Define the model to use
MODEL = "gpt-4o-mini"

# Define the client
client = OpenAI(api_key=os.getenv("OPEN_API_SECRET"))

questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
]

conversation = [
    {"role": "system", "content": "You are a helpful tourist guide, who will answer Parisian tourist questions."}
]

for question in questions:
    conversation.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model=MODEL,
        messages=conversation,
        max_tokens=100,
        temperature=0.0
    )

    answer = response.choices[0].message.content
    print(f"Q: {question}\nA: {answer}\n")
    conversation.append({"role": "assistant", "content": answer})
