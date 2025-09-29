# LinkedIn Post Automation

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Update `.env` file with your LinkedIn credentials:
```
LINKEDIN_EMAIL=your_email@example.com
LINKEDIN_PASSWORD=your_password
```

3. Customize posts in `posts.json`

## Usage

### Single Post
```bash
python linkedin_automation.py
```

### Scheduled Posts
```bash
python scheduler.py
```

## Features
- Automated login
- Post publishing
- Scheduled posting (9 AM & 3 PM daily)
- Queue management

## Security Notes
- Keep `.env` file private
- Use strong passwords
- Consider 2FA implications