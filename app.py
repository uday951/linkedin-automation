from flask import Flask, jsonify
from scheduler_bot import SmartScheduler
import threading
import json
from datetime import datetime
import requests
import time
import os

app = Flask(__name__)

# Self-ping to prevent sleep on Render free tier
def self_ping():
    if os.getenv('RENDER'):
        app_url = os.getenv('RENDER_EXTERNAL_URL', 'http://localhost:5000')
        while True:
            try:
                requests.get(f"{app_url}/ping", timeout=10)
                print(f"Self-ping successful at {datetime.now()}")
            except:
                print(f"Self-ping failed at {datetime.now()}")
            time.sleep(300)  # Ping every 5 minutes (300 seconds)

# Start scheduler in background thread
def start_scheduler():
    scheduler = SmartScheduler()
    scheduler.start_scheduler()

# Start threads when app starts
scheduler_thread = threading.Thread(target=start_scheduler, daemon=True)
ping_thread = threading.Thread(target=self_ping, daemon=True)

scheduler_thread.start()
ping_thread.start()

@app.route('/')
def home():
    return jsonify({
        "status": "LinkedIn Automation Bot Running",
        "message": "Posts 4 times per week automatically",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/ping')
def ping():
    return jsonify({
        "status": "alive",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/logs')
def get_logs():
    try:
        with open('post_log.json', 'r') as f:
            logs = json.load(f)
        return jsonify({"logs": logs[-10:]})  # Last 10 logs
    except:
        return jsonify({"logs": []})

@app.route('/status')
def status():
    try:
        with open('post_log.json', 'r') as f:
            logs = json.load(f)
        
        recent_logs = logs[-7:]  # Last 7 attempts
        successful_posts = len([log for log in recent_logs if log['success']])
        
        return jsonify({
            "posts_this_week": successful_posts,
            "last_post": logs[-1] if logs else None,
            "status": "active"
        })
    except:
        return jsonify({
            "posts_this_week": 0,
            "last_post": None,
            "status": "starting"
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)