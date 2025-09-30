import requests
import json
import os
from dotenv import load_dotenv
import google.generativeai as genai
import random
from datetime import datetime

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

#AIAgents #NewTools #SoftwareDevelopment #FutureOfWork #Developers" """,

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

#AIAgents #DevinAI #AutonomousCoding #FutureOfWork #Developers" """
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

def create_manual_post():
    """Create a post that can be manually copied to LinkedIn"""
    content = generate_ai_agent_post()
    
    # Save to file for manual posting
    with open('linkedin_post.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Log the generated post
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "content": content[:100] + "..." if len(content) > 100 else content,
        "method": "manual_file",
        "success": True
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
    
    print("✅ Post generated and saved to linkedin_post.txt")
    return content

if __name__ == "__main__":
    create_manual_post()