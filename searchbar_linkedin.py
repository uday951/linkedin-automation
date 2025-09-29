from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

def linkedin_post_searchbar(content):
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
        
        print("🔍 Looking for the search bar-like post input...")
        
        # Target the search bar with "Start a post" placeholder
        searchbar_selectors = [
            "//div[contains(text(), 'Start a post')]",
            "//input[contains(@placeholder, 'Start a post')]",
            "//div[contains(@placeholder, 'Start a post')]",
            "//button[contains(@aria-label, 'Start a post')]",
            "//div[@role='button' and contains(text(), 'Start a post')]",
            "//div[contains(@class, 'share-box-feed-entry__trigger')]",
            "//*[contains(@placeholder, 'Start a post')]",
            "//*[text()='Start a post']"
        ]
        
        clicked = False
        for selector in searchbar_selectors:
            try:
                searchbar = driver.find_element(By.XPATH, selector)
                print(f"✅ Found search bar with: {selector}")
                searchbar.click()
                clicked = True
                break
            except:
                continue
        
        if not clicked:
            print("❌ Could not find the search bar input")
            return False
            
        time.sleep(3)
        print("📝 Post dialog should be open, looking for text area...")
        
        # Look for the specific text area with "What do you want to talk about?" placeholder
        text_selectors = [
            "//div[contains(@data-placeholder, 'What do you want to talk about')]",
            "//div[contains(@aria-label, 'What do you want to talk about')]",
            "//div[@contenteditable='true' and contains(@data-placeholder, 'talk about')]",
            "//div[@contenteditable='true']",
            "//div[contains(@class, 'ql-editor')]"
        ]
        
        text_found = False
        for selector in text_selectors:
            try:
                text_area = driver.find_element(By.XPATH, selector)
                print(f"✅ Found text area: {selector}")
                
                # Make sure element is visible and clickable
                if text_area.is_displayed() and text_area.is_enabled():
                    text_area.click()
                    time.sleep(1)
                    text_area.clear()  # Clear any existing text
                    text_area.send_keys(content)
                    text_found = True
                    print(f"✅ Successfully added content to text area!")
                    break
                else:
                    print(f"❌ Text area not clickable: {selector}")
            except Exception as e:
                print(f"❌ Failed with {selector}: {str(e)[:50]}...")
                continue
        
        if not text_found:
            print("❌ Could not find text area")
            return False
            
        time.sleep(2)
        print("🚀 Looking for Post button...")
        
        # Look for Post button
        post_selectors = [
            "//span[text()='Post']",
            "//button[contains(text(), 'Post')]",
            "//button[contains(@aria-label, 'Post')]"
        ]
        
        for selector in post_selectors:
            try:
                post_btn = driver.find_element(By.XPATH, selector)
                print(f"✅ Found Post button: {selector}")
                post_btn.click()
                break
            except:
                continue
        
        time.sleep(3)
        print("✅ Post should be published!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        input("Press Enter to close...")
        driver.quit()

if __name__ == "__main__":
    linkedin_post_searchbar("Hello LinkedIn! Testing with search bar approach 🚀")