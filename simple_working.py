from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

def simple_linkedin_post(content):
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
        
        # Click Start a post using XPath
        start_post = driver.find_element(By.XPATH, "//*[text()='Start a post']")
        start_post.click()
        time.sleep(3)
        
        # Use JavaScript to add content
        script = f"""
        var editor = document.querySelector('div[contenteditable="true"]');
        if (editor) {{
            editor.focus();
            editor.innerHTML = '{content}';
            editor.dispatchEvent(new Event('input', {{bubbles: true}}));
            return 'SUCCESS';
        }}
        return 'FAILED';
        """
        
        result = driver.execute_script(script)
        print(f"Content result: {result}")
        
        if result == 'SUCCESS':
            time.sleep(2)
            # Click Post button
            post_btn = driver.find_element(By.XPATH, "//span[text()='Post']")
            post_btn.click()
            time.sleep(3)
            print("✅ Post published!")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        input("Press Enter to close...")
        driver.quit()

if __name__ == "__main__":
    simple_linkedin_post("Hello LinkedIn! Simple automation test 🚀")