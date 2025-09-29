from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

def setup_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        return driver
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure Chrome browser is installed and try again.")
        return None

def linkedin_post(content):
    load_dotenv()
    email = os.getenv('LINKEDIN_EMAIL')
    password = os.getenv('LINKEDIN_PASSWORD')
    
    driver = setup_chrome_driver()
    if not driver:
        return False
        
    try:
        # Login
        print("🔐 Logging in...")
        driver.get('https://www.linkedin.com/login')
        time.sleep(3)
        
        driver.find_element(By.ID, "username").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        time.sleep(8)  # Wait longer for login
        
        # Check if login successful
        if "feed" not in driver.current_url and "challenge" not in driver.current_url:
            driver.get('https://www.linkedin.com/feed/')
            time.sleep(5)
        
        print("📝 Creating post...")
        
        # Try multiple selectors for the search bar-like post input
        start_post_selectors = [
            "//div[contains(@class, 'share-box-feed-entry__trigger')]",
            "//button[contains(@class, 'share-box-feed-entry__trigger')]",
            "//div[contains(@data-test-id, 'share-box')]",
            "//input[contains(@placeholder, 'Start a post')]",
            "//div[contains(@role, 'button') and contains(@class, 'share-box')]",
            "//button[contains(@aria-label, 'Start a post')]",
            "//div[contains(@class, 'feed-shared-update-v2__commentary')]"
        ]
        
        start_post = None
        for selector in start_post_selectors:
            try:
                start_post = driver.find_element(By.XPATH, selector)
                break
            except:
                continue
                
        if not start_post:
            print("❌ Could not find 'Start a post' button")
            return False
            
        start_post.click()
        time.sleep(3)
        
        # Try multiple selectors for text area
        text_selectors = [
            "div[data-placeholder*='talk about']",
            "div[data-placeholder*='What do you want to talk about']",
            "div[contenteditable='true']",
            ".ql-editor"
        ]
        
        text_area = None
        for selector in text_selectors:
            try:
                text_area = driver.find_element(By.CSS_SELECTOR, selector)
                break
            except:
                continue
                
        if not text_area:
            print("❌ Could not find text area")
            return False
            
        text_area.click()
        text_area.send_keys(content)
        time.sleep(2)
        
        # Try multiple selectors for post button
        post_selectors = [
            "//span[text()='Post']",
            "//button[contains(@aria-label, 'Post')]",
            "//button[contains(text(), 'Post')]"
        ]
        
        post_button = None
        for selector in post_selectors:
            try:
                post_button = driver.find_element(By.XPATH, selector)
                break
            except:
                continue
                
        if not post_button:
            print("❌ Could not find Post button")
            return False
            
        post_button.click()
        time.sleep(3)
        
        print("✅ Post published successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Try manually checking if login worked or if LinkedIn requires verification")
        input("Press Enter to close browser...")
        return False
    finally:
        driver.quit()

if __name__ == "__main__":
    linkedin_post("Hello LinkedIn! Testing automation 🚀")