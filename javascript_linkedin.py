from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

def linkedin_post_js(content):
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
        result = driver.execute_script("""
            var startPost = document.evaluate("//*[text()='Start a post']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            if (startPost) {
                startPost.click();
                return 'CLICKED';
            } else {
                return 'NOT_FOUND';
            }
        """)
        print(f"🔍 Start post result: {result}")
        time.sleep(3)
        
        print("📝 Adding content using JavaScript...")
        
        # Use JavaScript to find and fill the text area
        js_script = f"""
        // Find the text area with various selectors
        var textArea = document.querySelector('div[data-placeholder*="What do you want to talk about"]') ||
                      document.querySelector('div[contenteditable="true"]') ||
                      document.querySelector('.ql-editor') ||
                      document.querySelector('div[role="textbox"]');
        
        if (textArea) {{
            textArea.focus();
            textArea.click();
            textArea.innerHTML = '{content}';
            textArea.innerText = '{content}';
            
            // Trigger input events
            var inputEvent = new Event('input', {{ bubbles: true }});
            var changeEvent = new Event('change', {{ bubbles: true }});
            textArea.dispatchEvent(inputEvent);
            textArea.dispatchEvent(changeEvent);
            
            return 'SUCCESS';
        }} else {{
            return 'TEXT_AREA_NOT_FOUND';
        }}
        """
        
        result = driver.execute_script(js_script)
        print(f"📝 JavaScript result: {result}")
        
        if result == 'SUCCESS':
            time.sleep(2)
            print("🚀 Clicking Post button...")
            
            # Click post button with JavaScript
            post_result = driver.execute_script("""
                var postBtn = document.evaluate("//span[text()='Post']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue ||
                             document.querySelector('button[aria-label*="Post"]');
                if (postBtn) {
                    postBtn.click();
                    return 'POST_CLICKED';
                } else {
                    return 'POST_NOT_FOUND';
                }
            """)
            print(f"🚀 Post button result: {post_result}")
            
            time.sleep(3)
            print("✅ Post should be published!")
            return True
        else:
            print("❌ Could not find or fill text area")
            return False
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        input("Press Enter to close...")
        driver.quit()

if __name__ == "__main__":
    linkedin_post_js("Hello LinkedIn! Testing JavaScript automation 🚀")