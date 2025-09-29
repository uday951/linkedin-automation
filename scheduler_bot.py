import schedule
import time
from gemini_linkedin import LinkedInGeminiBot
import random
from datetime import datetime, timedelta
import json
import os

class SmartScheduler:
    def __init__(self):
        self.bot = LinkedInGeminiBot()
        self.posts_this_week = 0
        self.last_reset = datetime.now()
        
    def should_post_today(self):
        # Load posting history
        try:
            with open('post_log.json', 'r') as f:
                logs = json.load(f)
                
            # Count posts this week
            week_start = datetime.now() - timedelta(days=7)
            recent_posts = [log for log in logs if datetime.fromisoformat(log['timestamp']) > week_start and log['success']]
            self.posts_this_week = len(recent_posts)
            
        except:
            self.posts_this_week = 0
        
        # Post if less than 4 posts this week
        if self.posts_this_week < 4:
            # Random chance to post (50% chance to make it 1-2 posts daily)
            return random.choice([True, False])
        
        return False
    
    def scheduled_post(self):
        if self.should_post_today():
            print(f"📅 Scheduled post triggered - Posts this week: {self.posts_this_week}")
            self.bot.run()
        else:
            print(f"⏭️ Skipping post - Already posted {self.posts_this_week} times this week")
    
    def start_scheduler(self):
        # Schedule posts at 9 AM and 3 PM daily
        schedule.every().day.at("09:00").do(self.scheduled_post)
        schedule.every().day.at("15:00").do(self.scheduled_post)
        
        print("🕐 Scheduler started - Posts will be published at 9 AM and 3 PM")
        print("📊 Target: 4 posts per week (1-2 daily)")
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

if __name__ == "__main__":
    scheduler = SmartScheduler()
    scheduler.start_scheduler()