import requests
import json
from datetime import datetime

def send_notification(content, webhook_url=None):
    """Send notification when post is ready"""
    
    notification_data = {
        "timestamp": datetime.now().isoformat(),
        "message": "New LinkedIn post ready!",
        "content_preview": content[:100] + "..." if len(content) > 100 else content,
        "action": "Copy from /latest-post and paste to LinkedIn"
    }
    
    # You can add webhook notifications here if needed
    if webhook_url:
        try:
            requests.post(webhook_url, json=notification_data, timeout=10)
        except:
            pass
    
    # Log notification
    print(f"🔔 NOTIFICATION: {notification_data['message']}")
    print(f"📝 Preview: {notification_data['content_preview']}")
    
    return True

def create_quick_access_page():
    """Create a simple HTML page for quick post access"""
    
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LinkedIn Post Ready</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
            .container { max-width: 600px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; }
            .post-content { background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0; }
            .copy-btn { background: #0077b5; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
            .copy-btn:hover { background: #005885; }
            .timestamp { color: #666; font-size: 12px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>🚀 LinkedIn Post Ready!</h2>
            <p>Your AI-generated post is ready to copy and paste to LinkedIn.</p>
            <div class="post-content" id="postContent">
                Loading post content...
            </div>
            <button class="copy-btn" onclick="copyPost()">📋 Copy Post</button>
            <p class="timestamp">Generated: <span id="timestamp"></span></p>
        </div>
        
        <script>
            async function loadPost() {
                try {
                    const response = await fetch('/latest-post');
                    const data = await response.json();
                    document.getElementById('postContent').innerText = data.post;
                    document.getElementById('timestamp').innerText = data.timestamp;
                } catch (error) {
                    document.getElementById('postContent').innerText = 'Error loading post';
                }
            }
            
            function copyPost() {
                const content = document.getElementById('postContent').innerText;
                navigator.clipboard.writeText(content).then(() => {
                    alert('Post copied! Now paste it to LinkedIn.');
                });
            }
            
            loadPost();
            setInterval(loadPost, 30000); // Refresh every 30 seconds
        </script>
    </body>
    </html>
    """
    
    return html_content

if __name__ == "__main__":
    # Test notification
    test_content = "Test post content for LinkedIn automation system 🚀 #AIAgents #Testing"
    send_notification(test_content)