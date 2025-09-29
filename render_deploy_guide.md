# Deploy to Render - Step by Step Guide

## Step 1: Test Locally First
```bash
python run_scheduler.py
```
This will post at 10:45 PM and 11:10 PM today, then continue daily.

## Step 2: Prepare for Deployment

### Create GitHub Repository
1. Go to https://github.com
2. Click "New repository"
3. Name it: `linkedin-automation`
4. Make it **Private** (to protect your credentials)
5. Click "Create repository"

### Upload Files to GitHub
```bash
git init
git add .
git commit -m "LinkedIn automation with AI agents"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/linkedin-automation.git
git push -u origin main
```

**Important**: Don't upload `.env` file (it's already in .gitignore)

## Step 3: Deploy to Render

### Create Render Account
1. Go to https://render.com
2. Click "Get Started"
3. Sign up with GitHub account

### Create Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository: `linkedin-automation`
3. Use these settings:

**Build Settings:**
- **Build Command**: `pip install -r requirements.txt && apt-get update && apt-get install -y wget gnupg && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && apt-get update && apt-get install -y google-chrome-stable`
- **Start Command**: `gunicorn app:app`

**Environment Variables:**
Click "Advanced" → Add these:
- `LINKEDIN_EMAIL` = `udaydd6062@gmail.com`
- `LINKEDIN_PASSWORD` = `Uday@m47`
- `GEMINI_API_KEY` = `AIzaSyB4ZLncr2aAMQjiS6fmQPB-JuUJQu67g44`
- `RENDER` = `true`

### Deploy
1. Click "Create Web Service"
2. Wait 5-10 minutes for deployment
3. Your app will be live at: `https://your-app-name.onrender.com`

## Step 4: Monitor

### Check Status
- **App Health**: `https://your-app-name.onrender.com/`
- **Post Logs**: `https://your-app-name.onrender.com/logs`
- **Status**: `https://your-app-name.onrender.com/status`

### What Happens After Deployment
✅ Posts automatically at 9 AM & 3 PM daily
✅ Generates fresh AI agent content each time
✅ Runs 24/7 without your intervention
✅ Logs all attempts for monitoring

## Troubleshooting

**If deployment fails:**
1. Check Render logs for errors
2. Verify environment variables are set
3. Make sure GitHub repo is connected

**If posts don't work:**
1. Check `/logs` endpoint
2. Verify LinkedIn credentials
3. Check Gemini API key

## Success!
Once deployed, your LinkedIn automation will:
- Generate unique AI agent posts in your style
- Post 4 times per week automatically
- Run forever without maintenance
- Track all activity in logs

Ready to deploy?