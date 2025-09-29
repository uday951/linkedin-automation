# Deployment Guide for Render

## Setup Steps

### 1. Get Gemini API Key
- Go to https://makersuite.google.com/app/apikey
- Create a new API key
- Copy the key

### 2. Update .env file
```
LINKEDIN_EMAIL=your_email@gmail.com
LINKEDIN_PASSWORD=your_password
GEMINI_API_KEY=your_actual_gemini_key
RENDER=true
```

### 3. Test Locally
```bash
pip install -r requirements.txt
python test_gemini.py
python gemini_linkedin.py
```

### 4. Deploy to Render

1. **Create Render Account**: https://render.com
2. **Connect GitHub**: Push this code to GitHub
3. **Create Web Service**:
   - Connect your GitHub repo
   - Use `render.yaml` configuration
   - Set environment variables:
     - `LINKEDIN_EMAIL`
     - `LINKEDIN_PASSWORD` 
     - `GEMINI_API_KEY`

### 5. Monitor

- **Status**: `https://your-app.onrender.com/status`
- **Logs**: `https://your-app.onrender.com/logs`
- **Health**: `https://your-app.onrender.com/`

## Features

✅ **Automated Content**: Gemini generates professional posts
✅ **Smart Scheduling**: 4 posts per week (1-2 daily)
✅ **Self-Managing**: No manual intervention needed
✅ **Monitoring**: Web dashboard for status
✅ **Logging**: Tracks all posting attempts

## Posting Schedule

- **Times**: 9 AM and 3 PM daily
- **Frequency**: 4 posts per week maximum
- **Content**: AI-generated professional posts
- **Topics**: Tech, productivity, motivation, trends

The system will automatically:
- Generate unique content using Gemini
- Post to LinkedIn at scheduled times
- Track posting history
- Maintain 4 posts per week limit
- Run 24/7 without intervention