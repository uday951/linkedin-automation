from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

def find_post_element():
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
        
        print("🔍 Searching for ALL elements with 'Start a post'...")
        
        # Find ALL elements containing "Start a post"
        all_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Start a post') or contains(@placeholder, 'Start a post') or contains(@aria-label, 'Start a post')]")
        
        print(f"📋 Found {len(all_elements)} elements:")
        
        for i, elem in enumerate(all_elements):
            try:
                print(f"\\n{i+1}. Tag: {elem.tag_name}")
                print(f"   Text: '{elem.text}'")
                print(f"   Placeholder: '{elem.get_attribute('placeholder')}'")
                print(f"   Class: '{elem.get_attribute('class')}'")
                print(f"   Clickable: {elem.is_enabled()}")
                
                # Try clicking this element
                if elem.is_enabled() and elem.is_displayed():
                    choice = input(f"   Try clicking element {i+1}? (y/n): ").lower()
                    if choice == 'y':
                        elem.click()
                        print("   ✅ Clicked!")
                        time.sleep(3)
                        
                        # Check if post dialog opened
                        try:
                            text_area = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true'], .ql-editor, textarea")
                            print("   🎯 Post dialog opened! Found text area.")
                            text_area.send_keys("Test post from automation! 🚀")
                            
                            # Look for post button
                            post_btn = driver.find_element(By.XPATH, "//span[text()='Post'] | //button[contains(text(), 'Post')]")
                            post_btn.click()
                            print("   ✅ Post published!")
                            break
                        except:
                            print("   ❌ No post dialog found")
                            
            except Exception as e:
                print(f"   ❌ Error with element {i+1}: {e}")
        
        input("\\nPress Enter to close...")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        input("Press Enter to close...")
    finally:
        driver.quit()

if __name__ == "__main__":
    find_post_element()