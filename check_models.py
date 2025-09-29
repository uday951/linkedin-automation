import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

print("Available models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"- {model.name}")
        
# Test with gemini-1.5-pro
try:
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content("Write a short LinkedIn post about AI")
    print(f"\nTest successful with gemini-1.5-pro:")
    print(response.text)
except Exception as e:
    print(f"Error with gemini-1.5-pro: {e}")
    
    # Try gemini-pro
    try:
        model = genai.GenerativeModel('models/gemini-pro')
        response = model.generate_content("Write a short LinkedIn post about AI")
        print(f"\nTest successful with models/gemini-pro:")
        print(response.text)
    except Exception as e2:
        print(f"Error with models/gemini-pro: {e2}")