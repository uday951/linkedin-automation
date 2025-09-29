from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

def debug_linkedin():
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
        
        print("⏳ Waiting for login... (10 seconds)")
        time.sleep(10)
        
        print(f"📍 Current URL: {driver.current_url}")
        
        if "challenge" in driver.current_url:
            print("🚨 LinkedIn requires verification. Please complete manually.")
            input("Complete verification and press Enter...")
        
        driver.get('https://www.linkedin.com/feed/')
        time.sleep(5)
        
        print("🔍 Looking for post elements...")
        
        # Find all clickable elements that might be the post button
        elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'post') or contains(text(), 'Post') or contains(text(), 'Start')]")
        
        print(f"📋 Found {len(elements)} potential elements:")
        for i, elem in enumerate(elements[:10]):  # Show first 10
            try:
                print(f"  {i+1}. Text: '{elem.text}' | Tag: {elem.tag_name}")
            except:
                print(f"  {i+1}. [Could not read element]")
        
        print("\n🎯 Manual intervention needed:")
        print("1. Look at the browser window")
        print("2. Find the 'Start a post' area")
        print("3. Note what text/button you see")
        
        input("Press Enter when ready to continue...")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        input("Press Enter to close browser...")
        driver.quit()

if __name__ == "__main__":
    debug_linkedin()