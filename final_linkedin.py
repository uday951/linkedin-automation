from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

def linkedin_post_final(content):
    load_dotenv()
    email = os.getenv('LINKEDIN_EMAIL')
    password = os.getenv('LINKEDIN_PASSWORD')
    
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    
    try:
        print("🔐 Logging in...")
        driver.get('https://www.linkedin.com/login')
        time.sleep(3)
        
        driver.find_element(By.ID, "username").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(8)
        
        driver.get('https://www.linkedin.com/feed/')
        time.sleep(5)
        
        print("🔍 Clicking 'Start a post'...")
        start_post = driver.find_element(By.XPATH, "//*[text()='Start a post']")
        start_post.click()
        time.sleep(3)
        
        print("📝 Looking for text area with 'What do you want to talk about?'...")
        
        # Try the exact placeholder text you mentioned
        text_area = driver.find_element(By.XPATH, "//div[contains(@data-placeholder, 'What do you want to talk about')]")
        text_area.click()
        time.sleep(1)
        
        # Use JavaScript to set the content directly
        driver.execute_script("arguments[0].innerHTML = arguments[1];", text_area, content)
        time.sleep(1)
        
        # Also try sending keys as backup
        text_area.send_keys(Keys.END)  # Move cursor to end
        text_area.send_keys(" ")  # Add space to trigger content detection
        
        time.sleep(2)
        print("🚀 Clicking Post button...")
        
        post_btn = driver.find_element(By.XPATH, "//span[text()='Post']")
        post_btn.click()
        
        time.sleep(3)
        print("✅ Post published successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        input("Press Enter to close...")
        driver.quit()

if __name__ == "__main__":
    linkedin_post_final("Hello LinkedIn! Final test of automation 🚀")