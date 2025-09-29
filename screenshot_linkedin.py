from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

def screenshot_linkedin():
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
        
        # Take screenshot after login
        driver.save_screenshot("after_login.png")
        print("📸 Screenshot saved: after_login.png")
        
        driver.get('https://www.linkedin.com/feed/')
        time.sleep(5)
        
        # Take screenshot of feed page
        driver.save_screenshot("linkedin_feed.png")
        print("📸 Screenshot saved: linkedin_feed.png")
        
        # Try to find elements with 'post' in them
        elements = driver.find_elements(By.XPATH, "//*[contains(translate(text(), 'POST', 'post'), 'post')]")
        print(f"🔍 Found {len(elements)} elements containing 'post':")
        
        for i, elem in enumerate(elements[:5]):
            try:
                print(f"  {i+1}. '{elem.text}' - Tag: {elem.tag_name}")
            except:
                print(f"  {i+1}. [Unreadable element]")
        
        print("\\n📋 Check the screenshots to see what LinkedIn is showing!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        input("Press Enter to close...")
        driver.quit()

if __name__ == "__main__":
    screenshot_linkedin()