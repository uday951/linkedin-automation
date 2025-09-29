import google.generativeai as genai
import os
from dotenv import load_dotenv

def test_gemini_simple():
    load_dotenv()
    
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY not found")
        return
    
    print("Testing Gemini content generation...")
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = "Write a professional LinkedIn post about productivity tips for developers. Keep it under 200 words with relevant hashtags."
        
        response = model.generate_content(prompt)
        content = response.text.strip()
        
        print("SUCCESS: Generated content:")
        print("-" * 50)
        print(content)
        print("-" * 50)
        
        return content
        
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    test_gemini_simple()