from flask import Flask, jsonify
from scheduler_bot import SmartScheduler
import threading
import json
from datetime import datetime

app = Flask(__name__)

# Start scheduler in background thread
def start_scheduler():
    scheduler = SmartScheduler()
    scheduler.start_scheduler()

# Start scheduler when app starts
scheduler_thread = threading.Thread(target=start_scheduler, daemon=True)
scheduler_thread.start()

@app.route('/')
def home():
    return jsonify({
        "status": "LinkedIn Automation Bot Running",
        "message": "Posts 4 times per week automatically",
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
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))