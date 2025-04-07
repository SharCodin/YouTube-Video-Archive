import os

from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
chat = client.chats.create(model="gemini-2.0-flash")
