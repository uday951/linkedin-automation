import requests
import time
import os
from datetime import datetime

def keep_render_alive():
    """Keep Render service alive by pinging every 5 minutes"""
    
    # Get the app URL from environment or use default
    app_url = os.getenv('RENDER_EXTERNAL_URL', 'http://localhost:5000')
    
    print(f"Starting keep-alive pinger for: {app_url}")
    
    while True:
        try:
            response = requests.get(f"{app_url}/ping", timeout=10)
            if response.status_code == 200:
                print(f"✅ Keep-alive ping successful at {datetime.now()}")
            else:
                print(f"⚠️ Keep-alive ping returned {response.status_code} at {datetime.now()}")
        except Exception as e:
            print(f"❌ Keep-alive ping failed at {datetime.now()}: {e}")
        
        # Wait 5 minutes before next ping
        time.sleep(300)

if __name__ == "__main__":
    keep_render_alive()