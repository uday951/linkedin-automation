import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import random
from dotenv import load_dotenv
import json
from datetime import datetime

class LinkedInGeminiBot:
    def __init__(self):
        load_dotenv()
        self.email = os.getenv('LINKEDIN_EMAIL')
        self.password = os.getenv('LINKEDIN_PASSWORD')
        self.gemini_key = os.getenv('GEMINI_API_KEY')
        
        # Configure Gemini
        genai.configure(api_key=self.gemini_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
    def generate_content(self):
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
            
            #AIAgents #CodeReview #SoftwareDevelopment #FutureOfWork #Developers""",
            
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
            
            #AIAgents #Testing #QualityAssurance #FutureOfWork #Developers""",
            
            """Write EXACTLY in this style:
            
            "AI deployment sounds effortless… until reality hits.
            
            AI agents can deploy code, manage containers, and scale systems faster than ever.
            But here's the hard truth 👇
            
            When things break at 3 AM, it's not just about "pushing code."
            It's about:
            
            Handling rollbacks & disaster recovery ⚡
            Managing database migrations & state 🔄
            Debugging production issues under pressure 💪
            
            This is why I keep saying:
            👉 DevOps isn't dead.
            👉 DevOps has evolved.
            
            AI agents can accelerate your deployments.
            But if you don't know infrastructure, monitoring, and incident response… you'll struggle when systems fail.
            
            So yes, use AI agents.
            But also learn to operate, not just deploy.
            
            That's where the real future of DevOps lies 🚀
            
            What do you think — will agents ever handle production incidents, or will that always need humans?
            
            #AIAgents #DevOps #Production #SystemDesign #Developers"""
        ]
        
        prompt = random.choice(prompts)
        
        try:
            response = self.model.generate_content(prompt)
            content = response.text.strip()
            print(f"SUCCESS: Generated content: {content[:100]}...")
            return content
        except Exception as e:
            print(f"ERROR: Gemini error: {e}")
            return "Excited to share insights about technology and innovation! 🚀 #tech #innovation #linkedin"
    
    def setup_driver(self):
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        
        # For Render deployment (Linux)
        if os.getenv('RENDER'):
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.binary_location = '/usr/bin/google-chrome'
            
        return webdriver.Chrome(options=options)
    
    def post_to_linkedin(self, content):
        driver = self.setup_driver()
        
        try:
            # Login
            driver.get('https://www.linkedin.com/login')
            time.sleep(3)
            
            driver.find_element(By.ID, "username").send_keys(self.email)
            driver.find_element(By.ID, "password").send_keys(self.password)
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
                print("SUCCESS: Post published successfully!")
                return True
            
            return False
            
        except Exception as e:
            print(f"ERROR: LinkedIn posting error: {e}")
            return False
        finally:
            driver.quit()
    
    def log_post(self, content, success):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "content": content[:100] + "..." if len(content) > 100 else content,
            "success": success
        }
        
        try:
            with open('post_log.json', 'r') as f:
                logs = json.load(f)
        except:
            logs = []
            
        logs.append(log_entry)
        
        # Keep only last 50 logs
        logs = logs[-50:]
        
        with open('post_log.json', 'w') as f:
            json.dump(logs, f, indent=2)
    
    def run(self):
        print(f"Starting LinkedIn automation at {datetime.now()}")
        
        # Generate content
        content = self.generate_content()
        
        # Post to LinkedIn
        success = self.post_to_linkedin(content)
        
        # Log the attempt
        self.log_post(content, success)
        
        if success:
            print("SUCCESS: Automation completed successfully!")
        else:
            print("ERROR: Automation failed!")

if __name__ == "__main__":
    bot = LinkedInGeminiBot()
    bot.run()