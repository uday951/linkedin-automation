import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
import random

def generate_ai_agent_post():
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompts = [
        """Write EXACTLY in this style:

"AI code review sounds perfect… until reality hits.

AI agents can scan code, catch bugs, and suggest fixes faster than ever.
But here's the hard truth 👇

When you ship to production, it's not just about "finding bugs."
It's about:

Understanding business context ⚡
Catching architectural anti-patterns 🔄
Reviewing for security vulnerabilities that matter 💪

This is why I keep saying:
👉 Code review isn't dead.
👉 Code review has evolved.

AI agents can accelerate your reviews.
But if you don't know design patterns, security principles, and system architecture… you'll miss the issues that actually break systems.

So yes, use AI agents.
But also learn to architect, not just syntax-check.

That's where the real future of developers lies 🚀

What do you think — will agents ever understand business requirements, or will that always need humans?

#AIAgents #CodeReview #SoftwareDevelopment #FutureOfWork #Developers" """,

        """Write EXACTLY in this style:

"AI testing sounds amazing… until reality hits.

AI agents can generate tests, run scenarios, and catch regressions faster than ever.
But here's the hard truth 👇

When users hit your app, it's not just about "running tests."
It's about:

Testing real user journeys ⚡
Handling edge cases & data variations 🔄
Validating business logic that changes constantly 💪

This is why I keep saying:
👉 Testing isn't dead.
👉 Testing has evolved.

AI agents can accelerate your testing.
But if you don't know user behavior, business rules, and system boundaries… you'll miss the scenarios that actually matter.

So yes, use AI agents.
But also learn to strategize, not just automate.

That's where the real future of QA lies 🚀

What do you think — will agents ever grasp user experience, or will that always need humans?

#AIAgents #Testing #QualityAssurance #FutureOfWork #Developers" """
    ]
    
    prompt = random.choice(prompts)
    
    try:
        response = model.generate_content(prompt)
        content = response.text.strip()
        print(f"✅ Generated AI agent post: {content[:100]}...")
        return content
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "AI agents are transforming development… but human expertise still matters! 🚀 #AIAgents #Developers"

def post_to_linkedin(content):
    load_dotenv()
    email = os.getenv('LINKEDIN_EMAIL')
    password = os.getenv('LINKEDIN_PASSWORD')
    
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    
    try:
        print("🔐 Logging into LinkedIn...")
        driver.get('https://www.linkedin.com/login')
        time.sleep(3)
        
        driver.find_element(By.ID, "username").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(8)
        
        print("📱 Going to LinkedIn feed...")
        driver.get('https://www.linkedin.com/feed/')
        time.sleep(5)
        
        print("🎯 Clicking 'Start a post'...")
        start_post = driver.find_element(By.XPATH, "//*[text()='Start a post']")
        start_post.click()
        time.sleep(3)
        
        print("📝 Adding content...")
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
            print("🚀 Publishing post...")
            time.sleep(2)
            post_btn = driver.find_element(By.XPATH, "//span[text()='Post']")
            post_btn.click()
            time.sleep(3)
            print("✅ SUCCESS: Post published to LinkedIn!")
            return True
        else:
            print("❌ Failed to add content")
            return False
        
    except Exception as e:
        print(f"❌ LinkedIn error: {e}")
        return False
    finally:
        input("Press Enter to close browser...")
        driver.quit()

def test_complete_automation():
    print("🤖 TESTING COMPLETE LINKEDIN AUTOMATION")
    print("=" * 50)
    
    # Step 1: Generate AI agent content
    print("Step 1: Generating AI agent post with Gemini...")
    content = generate_ai_agent_post()
    
    # Show generated content
    print("\n📄 GENERATED CONTENT:")
    print("-" * 30)
    content_clean = content.encode('ascii', 'ignore').decode('ascii')
    print(content_clean)
    print("-" * 30)
    
    # Step 2: Post to LinkedIn
    print("\nStep 2: Posting to LinkedIn...")
    success = post_to_linkedin(content)
    
    # Final result
    if success:
        print("\n🎉 COMPLETE SUCCESS!")
        print("✅ Gemini generated AI agent post")
        print("✅ Posted to LinkedIn successfully")
        print("✅ Full automation working!")
    else:
        print("\n❌ AUTOMATION FAILED")
        print("Content generation worked, but LinkedIn posting failed")

if __name__ == "__main__":
    test_complete_automation()