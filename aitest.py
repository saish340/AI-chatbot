import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List all available models
models = genai.list_models()
for model in models:
    print(model.name)
