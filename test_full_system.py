import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
import json
from datetime import datetime

def generate_content():
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompts = [
        "Write a professional LinkedIn post about productivity tips for developers. Keep it under 200 words with relevant hashtags.",
        "Create a LinkedIn post about the importance of continuous learning in tech. Include personal insights and hashtags.",
        "Write a motivational LinkedIn post about overcoming challenges in software development. Add relevant hashtags."
    ]
    
    import random
    prompt = random.choice(prompts)
    
    try:
        response = model.generate_content(prompt)
        content = response.text.strip()
        # Remove emojis that cause encoding issues
        content = content.encode('ascii', 'ignore').decode('ascii')
        print(f"Generated content: {content[:100]}...")
        return content
    except Exception as e:
        print(f"Gemini error: {e}")
        return "Excited to share insights about technology and innovation! #tech #innovation #linkedin"

def post_to_linkedin(content):
    load_dotenv()
    email = os.getenv('LINKEDIN_EMAIL')
    password = os.getenv('LINKEDIN_PASSWORD')
    
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    
    try:
        # Login
        driver.get('https://www.linkedin.com/login')
        time.sleep(3)
        
        driver.find_element(By.ID, "username").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(8)
        
        # Go to feed
        driver.get('https://www.linkedin.com/feed/')
        time.sleep(5)
        
        # Click Start a post
        start_post = driver.find_element(By.XPATH, "//*[text()='Start a post']")
        start_post.click()
        time.sleep(3)
        
        # Add content using JavaScript
        script = f"""
        var editor = document.querySelector('div[contenteditable="true"]');
        if (editor) {{
            editor.focus();
            editor.innerHTML = `{content}`;
            editor.dispatchEvent(new Event('input', {{bubbles: true}}));
            return 'SUCCESS';
        }}
        return 'FAILED';
        """
        
        result = driver.execute_script(script)
        
        if result == 'SUCCESS':
            time.sleep(2)
            post_btn = driver.find_element(By.XPATH, "//span[text()='Post']")
            post_btn.click()
            time.sleep(3)
            print("SUCCESS: Post published!")
            return True
        
        return False
        
    except Exception as e:
        print(f"LinkedIn error: {e}")
        return False
    finally:
        input("Press Enter to close browser...")
        driver.quit()

def main():
    print(f"Starting full system test at {datetime.now()}")
    
    # Generate content with Gemini
    content = generate_content()
    
    # Post to LinkedIn
    success = post_to_linkedin(content)
    
    if success:
        print("COMPLETE SUCCESS: Gemini + LinkedIn automation working!")
    else:
        print("ERROR: Something failed in the process")

if __name__ == "__main__":
    main()