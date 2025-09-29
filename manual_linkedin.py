from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

def manual_linkedin_post(content):
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
        
        print("⏳ Waiting for login...")
        time.sleep(8)
        
        print(f"📍 Current URL: {driver.current_url}")
        
        # Go to feed
        driver.get('https://www.linkedin.com/feed/')
        time.sleep(5)
        
        print("🔍 Browser is open. Please:")
        print("1. Check if you're logged in properly")
        print("2. Look for any verification prompts")
        print("3. Find the 'Start a post' button manually")
        print("4. If you see it, note its exact text/location")
        
        # Keep browser open for manual inspection
        choice = input("\\nDo you see the 'Start a post' button? (y/n): ").lower()
        
        if choice == 'y':
            print("\\n🎯 Trying to find and click the post button...")
            
            # Extended list of selectors
            selectors = [
                "//span[contains(text(), 'Start a post')]",
                "//button[contains(text(), 'Start a post')]",
                "//div[contains(text(), 'Start a post')]",
                "//*[contains(text(), 'Start a post')]",
                "//button[contains(@aria-label, 'Start a post')]",
                "//div[contains(@class, 'share-box')]",
                "//div[contains(@data-test-id, 'share-box')]",
                "//button[contains(@class, 'share-box')]"
            ]
            
            clicked = False
            for selector in selectors:
                try:
                    element = driver.find_element(By.XPATH, selector)
                    print(f"✅ Found element with selector: {selector}")
                    element.click()
                    clicked = True
                    break
                except Exception as e:
                    print(f"❌ Failed selector: {selector}")
                    continue
            
            if clicked:
                time.sleep(3)
                print("🎯 Looking for text area...")
                
                # Try to find text area
                text_selectors = [
                    "div[contenteditable='true']",
                    ".ql-editor",
                    "div[data-placeholder*='talk']",
                    "textarea"
                ]
                
                for selector in text_selectors:
                    try:
                        text_area = driver.find_element(By.CSS_SELECTOR, selector)
                        print(f"✅ Found text area: {selector}")
                        text_area.click()
                        text_area.send_keys(content)
                        print("✅ Content added!")
                        
                        # Look for post button
                        time.sleep(2)
                        post_btn = driver.find_element(By.XPATH, "//span[text()='Post'] | //button[contains(text(), 'Post')]")
                        post_btn.click()
                        print("✅ Post published!")
                        break
                    except Exception as e:
                        print(f"❌ Text area selector failed: {selector}")
                        continue
            else:
                print("❌ Could not find post button automatically")
        
        input("\\nPress Enter to close browser...")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        input("Press Enter to close browser...")
    finally:
        driver.quit()

if __name__ == "__main__":
    manual_linkedin_post("Hello LinkedIn! Testing manual automation 🚀")