from gemini_linkedin import LinkedInGeminiBot
import os
from dotenv import load_dotenv

def test_gemini():
    load_dotenv()
    
    # Check if API key is set
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key or api_key == 'your_gemini_api_key_here':
        print("❌ Please set your GEMINI_API_KEY in .env file")
        print("Get it from: https://makersuite.google.com/app/apikey")
        return
    
    bot = LinkedInGeminiBot()
    
    print("🧪 Testing Gemini content generation...")
    content = bot.generate_content()
    print(f"✅ Generated content:\n{content}")
    
    print("\n🧪 Testing LinkedIn posting (without actually posting)...")
    print("Content would be posted to LinkedIn")

if __name__ == "__main__":
    test_gemini()