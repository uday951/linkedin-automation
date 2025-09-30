#!/usr/bin/env python3
"""
LinkedIn Automation for Hostinger VPS
Run this script on your Hostinger VPS for fully automated LinkedIn posting
"""

import os
import subprocess
import sys
from datetime import datetime

def setup_display():
    """Setup virtual display for Chrome on headless server"""
    try:
        # Kill any existing Xvfb processes
        subprocess.run(['pkill', 'Xvfb'], stderr=subprocess.DEVNULL)
        
        # Start Xvfb virtual display
        subprocess.Popen(['Xvfb', ':99', '-screen', '0', '1920x1080x24'], 
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Set display environment variable
        os.environ['DISPLAY'] = ':99'
        print("✅ Virtual display setup complete")
        return True
    except Exception as e:
        print(f"❌ Display setup failed: {e}")
        return False

def check_chrome():
    """Check if Chrome is installed and working"""
    try:
        result = subprocess.run(['google-chrome', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Chrome installed: {result.stdout.strip()}")
            return True
        else:
            print("❌ Chrome not found")
            return False
    except Exception as e:
        print(f"❌ Chrome check failed: {e}")
        return False

def main():
    print(f"🚀 Starting LinkedIn Automation on Hostinger VPS at {datetime.now()}")
    
    # Setup virtual display
    if not setup_display():
        print("❌ Failed to setup display. Install xvfb: sudo apt install xvfb")
        sys.exit(1)
    
    # Check Chrome installation
    if not check_chrome():
        print("❌ Chrome not installed. Run hostinger_setup.sh first")
        sys.exit(1)
    
    # Import and run the main app
    try:
        from app import app
        print("✅ Starting Flask app...")
        print("📱 Access at: http://your-vps-ip:5000")
        print("📊 Status at: http://your-vps-ip:5000/status")
        print("📝 Logs at: http://your-vps-ip:5000/logs")
        
        # Run the app
        app.run(host='0.0.0.0', port=5000, debug=False)
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure you're in the right directory and virtual environment is activated")
        sys.exit(1)
    except Exception as e:
        print(f"❌ App error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()