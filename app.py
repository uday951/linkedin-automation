from flask import Flask, jsonify, send_file
import threading
import json
from datetime import datetime
import requests
import time
import os
import schedule
import google.generativeai as genai
from dotenv import load_dotenv
import random

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

def generate_ai_agent_post():
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompts = [
        """Write EXACTLY in this style:

"New AI coding agents launch every week… until you try them in production.

GitHub Copilot, Cursor, Replit Agent, and CodeWhisperer promise to revolutionize development.
But here's the hard truth 👇

When you build real systems, it's not just about "generating code."
It's about:

Integrating with legacy systems ⚡
Handling edge cases & error scenarios 🔄
Maintaining code that others can understand 💪

This is why I keep saying:
👉 Coding isn't dead.
👉 Coding has evolved.

New AI agents can accelerate your development.
But if you don't know system design, debugging, and architecture patterns… you'll struggle when the generated code breaks.

So yes, try every new agent.
But also learn to think, not just prompt.

That's where the real future of developers lies 🚀

What do you think — which new AI agent has impressed you most, or are they all just hype?

#AIAgents #NewTools #SoftwareDevelopment #FutureOfWork #Developers"""
    ]
    
    prompt = random.choice(prompts)
    
    try:
        response = model.generate_content(prompt)
        content = response.text.strip()
        print(f"Generated content: {content[:100]}...")
        return content
    except Exception as e:
        print(f"Gemini error: {e}")
        return "AI agents are transforming development… but human expertise still matters! 🚀 #AIAgents #Developers"

def save_post_for_manual_use(content):
    """Save post to file for manual copying to LinkedIn"""
    try:
        with open('linkedin_post.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Post saved to linkedin_post.txt for manual posting")
        return True
    except Exception as e:
        print(f"Error saving post: {e}")
        return False

def scheduled_post():
    print(f"🚀 Scheduled post triggered at {datetime.now()}")
    
    content = generate_ai_agent_post()
    success = save_post_for_manual_use(content)
    
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "content": content[:100] + "..." if len(content) > 100 else content,
        "method": "generated_for_manual_posting",
        "success": success
    }
    
    try:
        with open('post_log.json', 'r') as f:
            logs = json.load(f)
    except:
        logs = []
        
    logs.append(log_entry)
    logs = logs[-50:]
    
    with open('post_log.json', 'w') as f:
        json.dump(logs, f, indent=2)
    
    if success:
        print("🎉 Post generated successfully! Check /download-post to get it")
    else:
        print("❌ Post generation failed!")

# Start scheduler in background thread
def start_scheduler():
    # Test post in 2 minutes from now
    from datetime import datetime, timedelta
    test_time = (datetime.now() + timedelta(minutes=2)).strftime("%H:%M")
    schedule.every().day.at(test_time).do(scheduled_post)
    
    # Regular schedule
    schedule.every().day.at("09:00").do(scheduled_post)
    schedule.every().day.at("15:00").do(scheduled_post)
    
    print(f"Scheduler started - Test post at {test_time}")
    print("Regular posts at 9 AM and 3 PM")
    print("Posts will be generated and available at /latest-post")
    print("Target: 4 posts per week (1-2 daily)")
    
    while True:
        schedule.run_pending()
        time.sleep(60)

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

@app.route('/download-post')
def download_post():
    try:
        return send_file('linkedin_post.txt', as_attachment=True, download_name='linkedin_post.txt')
    except:
        return jsonify({"error": "No post available"})

@app.route('/latest-post')
def latest_post():
    try:
        with open('linkedin_post.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        return jsonify({
            "post": content,
            "timestamp": datetime.now().isoformat(),
            "instructions": "Copy this content and paste it manually to LinkedIn"
        })
    except:
        return jsonify({"error": "No post available"})

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