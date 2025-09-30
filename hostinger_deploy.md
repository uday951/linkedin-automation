# Deploy to Hostinger VPS - BEST Option for LinkedIn Automation

## Why Hostinger VPS?
✅ **Full Chrome support** - No limitations
✅ **Very affordable** - $3.99/month VPS
✅ **Complete control** - Install anything
✅ **Better than free platforms** - More reliable
✅ **Perfect for automation** - No restrictions

## Step 1: Get Hostinger VPS
1. Go to https://hostinger.com
2. Choose "VPS Hosting" 
3. Select cheapest plan ($3.99/month)
4. Choose Ubuntu 20.04 or 22.04
5. Complete purchase and get VPS details

## Step 2: Connect to VPS
```bash
ssh root@your-vps-ip
# Enter password from Hostinger email
```

## Step 3: Setup Environment
```bash
# Download and run setup script
wget https://raw.githubusercontent.com/your-username/linkedin-automation/main/hostinger_setup.sh
chmod +x hostinger_setup.sh
./hostinger_setup.sh
```

## Step 4: Upload Your Project
```bash
# In your local machine
scp -r "C:\Users\Udayk\Desktop\linkdin automation" root@your-vps-ip:~/linkedin-automation/
```

## Step 5: Configure Environment
```bash
# On VPS
cd ~/linkedin-automation
source venv/bin/activate

# Create .env file
cat > .env << EOF
LINKEDIN_EMAIL=udaydd6062@gmail.com
LINKEDIN_PASSWORD=Uday@m47
GEMINI_API_KEY=AIzaSyB4ZLncr2aAMQjiS6fmQPB-JuUJQu67g44
HOSTINGER_VPS=true
EOF
```

## Step 6: Start Virtual Display (for Chrome)
```bash
# Install and start Xvfb (virtual display)
sudo apt install xvfb -y
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99
```

## Step 7: Run the Application
```bash
# Test run
python3 app.py

# Or run with gunicorn
gunicorn app:app --bind 0.0.0.0:5000
```

## Step 8: Setup as Service (Auto-start)
```bash
# Create systemd service
sudo tee /etc/systemd/system/linkedin-automation.service > /dev/null <<EOF
[Unit]
Description=LinkedIn Automation
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/linkedin-automation
Environment=PATH=/root/linkedin-automation/venv/bin
Environment=DISPLAY=:99
ExecStartPre=/usr/bin/Xvfb :99 -screen 0 1920x1080x24
ExecStart=/root/linkedin-automation/venv/bin/gunicorn app:app --bind 0.0.0.0:5000
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
sudo systemctl enable linkedin-automation
sudo systemctl start linkedin-automation
sudo systemctl status linkedin-automation
```

## Step 9: Access Your App
- **App URL**: `http://your-vps-ip:5000`
- **Status**: `http://your-vps-ip:5000/status`
- **Logs**: `http://your-vps-ip:5000/logs`

## What You Get
✅ **Fully automated** LinkedIn posting
✅ **Test post in 2 minutes** after setup
✅ **Daily posts at 9 AM & 3 PM**
✅ **Runs 24/7** automatically
✅ **No restrictions** like free platforms
✅ **Full Chrome support**
✅ **Complete control**

## Cost Comparison
- **Hostinger VPS**: $3.99/month - FULL automation
- **Railway Free**: $0/month - Limited features
- **Render Free**: $0/month - Doesn't work for this

## Hostinger is the BEST choice for reliable LinkedIn automation!

**Ready to set up on Hostinger VPS?**