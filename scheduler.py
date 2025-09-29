import schedule
import time
from linkedin_automation import LinkedInAutomation
import json

class PostScheduler:
    def __init__(self):
        self.posts_queue = []
        
    def load_posts(self, filename='posts.json'):
        try:
            with open(filename, 'r') as f:
                self.posts_queue = json.load(f)
        except FileNotFoundError:
            print("No posts file found. Create posts.json with your content.")
            
    def post_content(self):
        if not self.posts_queue:
            print("No posts in queue")
            return
            
        automation = LinkedInAutomation()
        try:
            automation.setup_driver()
            automation.login()
            
            post = self.posts_queue.pop(0)
            automation.create_post(post['content'])
            
            # Save remaining posts
            with open('posts.json', 'w') as f:
                json.dump(self.posts_queue, f, indent=2)
                
        finally:
            automation.close()
            
    def schedule_posts(self):
        schedule.every().day.at("09:00").do(self.post_content)
        schedule.every().day.at("15:00").do(self.post_content)
        
        print("Scheduler started. Posts will be published at 9 AM and 3 PM daily.")
        
        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    scheduler = PostScheduler()
    scheduler.load_posts()
    scheduler.schedule_posts()