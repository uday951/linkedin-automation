from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv

class LinkedInAutomation:
    def __init__(self):
        load_dotenv()
        self.email = os.getenv('LINKEDIN_EMAIL')
        self.password = os.getenv('LINKEDIN_PASSWORD')
        self.driver = None
        
    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--remote-debugging-port=9222')
        
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
        except Exception as e:
            print(f"Chrome setup failed: {e}")
            print("Trying alternative setup...")
            self.driver = webdriver.Chrome(options=options)
        
    def login(self):
        self.driver.get('https://www.linkedin.com/login')
        
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        email_field.send_keys(self.email)
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(self.password)
        
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        
        time.sleep(3)
        
    def create_post(self, content):
        self.driver.get('https://www.linkedin.com/feed/')
        
        start_post = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Start a post']"))
        )
        start_post.click()
        
        text_area = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-placeholder='What do you want to talk about?']"))
        )
        text_area.send_keys(content)
        
        post_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Post']"))
        )
        post_button.click()
        
        time.sleep(2)
        print("Post published successfully!")
        
    def close(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    automation = LinkedInAutomation()
    try:
        automation.setup_driver()
        automation.login()
        automation.create_post("Hello LinkedIn! This is an automated post. 🚀")
    finally:
        automation.close()