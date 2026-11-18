import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load your secret key from the .env file
load_dotenv()
my_key = os.getenv("OPENROUTER_API_KEY")

if not my_key:
    raise ValueError("OPENROUTER_API_KEY not found! Check your .env file.")

# 2. Connect to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=my_key,
)

# 3. Ask a free AI model a question
print("Thinking...")
response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {"role": "user", "content": "What is Artificial Intelligence? Explain in simple words."}
    ]
)

# 4. Print which model answered + the response
print(f"\nModel used: {response.model}")
print("\nLLM Response:")
print(response.choices[0].message.content)