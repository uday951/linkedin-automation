import schedule
import time
from datetime import datetime
import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import random
import json

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

#AIAgents #NewTools #SoftwareDevelopment #FutureOfWork #Developers""",

        """Write EXACTLY in this style:

"Devin AI agent sounds revolutionary… until you see the demo limitations.

Cognition Labs claims their AI can build entire apps, fix bugs, and deploy systems autonomously.
But here's the hard truth 👇

When you need real software, it's not just about "autonomous coding."
It's about:

Understanding business requirements ⚡
Handling complex integrations & APIs 🔄
Debugging issues that require domain knowledge 💪

This is why I keep saying:
👉 Software engineering isn't dead.
👉 Software engineering has evolved.

Devin and similar agents can handle simple tasks.
But if you don't know system architecture, user needs, and technical trade-offs… you'll build the wrong thing faster.

So yes, watch these agents.
But also learn to engineer, not just automate.

That's where the real future of developers lies 🚀

What do you think — will autonomous coding agents replace developers, or just change how we work?

#AIAgents #DevinAI #AutonomousCoding #FutureOfWork #Developers""",

        """Write EXACTLY in this style:

"Claude Dev and ChatGPT Code Interpreter sound amazing… until you need production-ready code.

These AI agents can write scripts, analyze data, and even build small apps in minutes.
But here's the hard truth 👇

When you ship to users, it's not just about "working code."
It's about:

Optimizing for performance & scalability ⚡
Handling security & data privacy 🔄
Building maintainable & testable systems 💪

This is why I keep saying:
👉 Development isn't dead.
👉 Development has evolved.

AI interpreters can prototype quickly.
But if you don't know software engineering principles, testing, and system design… you'll ship code that breaks under load.

So yes, use these tools for rapid prototyping.
But also learn to build, not just generate.

That's where the real future of developers lies 🚀

What do you think — are code interpreters changing how you prototype, or just creating more technical debt?

#AIAgents #ClaudeDev #CodeInterpreter #RapidPrototyping #Developers""",

        """Write EXACTLY in this style:

"Windsurf Editor and Bolt.new promise AI-first development… until you hit complex requirements.

These new AI-powered IDEs can scaffold projects, write components, and even deploy apps automatically.
But here's the hard truth 👇

When you build real products, it's not just about "AI-generated scaffolding."
It's about:

Customizing for specific business logic ⚡
Integrating with existing systems & databases 🔄
Optimizing for user experience & performance 💪

This is why I keep saying:
👉 Development tools aren't dead.
👉 Development tools have evolved.

AI-first editors can speed up initial development.
But if you don't know component architecture, state management, and UX principles… you'll build apps that look good but work poorly.

So yes, try these new editors.
But also learn to craft, not just scaffold.

That's where the real future of developers lies 🚀

What do you think — will AI-first IDEs replace traditional development, or just change our workflow?

#AIAgents #WindsurfEditor #BoltNew #AIDevelopment #Developers""",

        """Write EXACTLY in this style:

"Aider, Continue, and Codeium promise perfect AI pair programming… until you need to debug complex issues.

These AI coding assistants can refactor code, suggest improvements, and even write tests automatically.
But here's the hard truth 👇

When systems fail in production, it's not just about "AI suggestions."
It's about:

Understanding root causes & system interactions ⚡
Debugging across multiple services & databases 🔄
Fixing issues under time pressure & user impact 💪

This is why I keep saying:
👉 Debugging isn't dead.
👉 Debugging has evolved.

AI pair programming can help with routine tasks.
But if you don't know system architecture, logging, and troubleshooting… you'll struggle when AI can't solve the problem.

So yes, pair with AI assistants.
But also learn to debug, not just code.

That's where the real future of developers lies 🚀

What do you think — has AI pair programming made you a better debugger, or more dependent on suggestions?

#AIAgents #AIPairProgramming #Debugging #SoftwareDevelopment #Developers"""
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

def post_to_linkedin(content):
    load_dotenv()
    email = os.getenv('LINKEDIN_EMAIL')
    password = os.getenv('LINKEDIN_PASSWORD')
    
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    
    try:
        print("Logging into LinkedIn...")
        driver.get('https://www.linkedin.com/login')
        time.sleep(3)
        
        driver.find_element(By.ID, "username").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(8)
        
        driver.get('https://www.linkedin.com/feed/')
        time.sleep(5)
        
        start_post = driver.find_element(By.XPATH, "//*[text()='Start a post']")
        start_post.click()
        time.sleep(3)
        
        script = f"""
        var editor = document.querySelector('div[contenteditable="true"]');
        if (editor) {{
            editor.focus();
            editor.innerHTML = `{content}`;
            editor.dispatchEvent(new Event('input', {{bubbles: true}}));
            return 'SUCCESS';
        }}
        return 'FAILED';
        """
        
        result = driver.execute_script(script)
        
        if result == 'SUCCESS':
            time.sleep(2)
            post_btn = driver.find_element(By.XPATH, "//span[text()='Post']")
            post_btn.click()
            time.sleep(3)
            print("SUCCESS: Post published!")
            return True
        
        return False
        
    except Exception as e:
        print(f"LinkedIn error: {e}")
        return False
    finally:
        driver.quit()

def log_post(content, success):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "content": content[:100] + "..." if len(content) > 100 else content,
        "success": success
    }
    
    try:
        with open('post_log.json', 'r') as f:
            logs = json.load(f)
    except:
        logs = []
        
    logs.append(log_entry)
    logs = logs[-50:]  # Keep last 50 logs
    
    with open('post_log.json', 'w') as f:
        json.dump(logs, f, indent=2)

def scheduled_post():
    print(f"Scheduled post triggered at {datetime.now()}")
    
    # Generate AI agent content
    content = generate_ai_agent_post()
    
    # Post to LinkedIn
    success = post_to_linkedin(content)
    
    # Log the attempt
    log_post(content, success)
    
    if success:
        print("Automation completed successfully!")
    else:
        print("Automation failed!")

def start_scheduler():
    # Test posts today
    schedule.every().day.at("22:45").do(scheduled_post)  # 10:45 PM today
    schedule.every().day.at("23:10").do(scheduled_post)  # 11:10 PM today
    
    # Regular schedule: 9 AM and 3 PM daily
    schedule.every().day.at("09:00").do(scheduled_post)
    schedule.every().day.at("15:00").do(scheduled_post)
    
    print(f"Scheduler started at {datetime.now()}")
    print("Test posts scheduled for:")
    print("- Today at 10:45 PM")
    print("- Today at 11:10 PM")
    print("- Then daily at 9:00 AM and 3:00 PM")
    print("Press Ctrl+C to stop")
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    start_scheduler()