from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import os
from dotenv import load_dotenv

def linkedin_post_edge(content):
    load_dotenv()
    email = os.getenv('LINKEDIN_EMAIL')
    password = os.getenv('LINKEDIN_PASSWORD')
    
    options = webdriver.EdgeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    try:
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
    except:
        driver = webdriver.Edge(options=options)
    
    try:
        driver.get('https://www.linkedin.com/login')
        time.sleep(2)
        
        driver.find_element(By.ID, "username").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        
        driver.get('https://www.linkedin.com/feed/')
        time.sleep(3)
        
        start_post = driver.find_element(By.XPATH, "//span[contains(text(), 'Start a post')]")
        start_post.click()
        time.sleep(2)
        
        text_area = driver.find_element(By.CSS_SELECTOR, "div[data-placeholder*='talk about']")
        text_area.send_keys(content)
        time.sleep(1)
        
        post_button = driver.find_element(By.XPATH, "//span[text()='Post']")
        post_button.click()
        time.sleep(3)
        
        print("✅ Post published successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        driver.quit()

if __name__ == "__main__":
    linkedin_post_edge("Hello LinkedIn! Testing with Edge browser 🚀")