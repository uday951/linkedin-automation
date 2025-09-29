import google.generativeai as genai
import os
from dotenv import load_dotenv
import random

def test_style_generation():
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Your style prompts for AI agents
    prompts = [
        """Write a LinkedIn post about AI agents for code review in this exact style:

STYLE EXAMPLE:
"Vibe coding sounds cool… until reality hits.

AI agents can write code, debug errors, and even build apps faster than ever.
But here's the hard truth 👇

When your system goes live, it's not just about "generating code."
It's about:

Handling rate limits ⚡
Designing retries & fallbacks 🔄
Building idempotent systems that don't break under pressure 💪

This is why I keep saying:
👉 Coding isn't dead.
👉 Coding has evolved.

AI agents can accelerate you.
But if you don't know the fundamentals, frameworks, and real-world practices… you'll struggle the moment things get serious.

So yes, use agents.
But also learn to architect, not just copy-paste.

That's where the real future of developers lies 🚀

What do you think — will agents ever learn to handle real-world system design, or will that always need humans?"

TOPIC: AI agents for code review
REQUIREMENTS:
- Start with catchy hook about AI code review
- Reality check with "But here's the hard truth 👇"
- Bullet points with emojis about real challenges
- Use 👉 for key points
- End with engaging question
- Hashtags: #AIAgents #CodeReview #SoftwareDevelopment #FutureOfWork #Developers""",

        """Write a LinkedIn post about AI agents for testing in the same style as above.
TOPIC: AI agents writing and running tests
- Hook about automated testing with AI
- Reality check about what they miss
- Bullet points about edge cases, user scenarios, business logic
- Key points with 👉
- Question about future of QA engineers
- Hashtags: #AIAgents #Testing #QualityAssurance #Automation #Developers""",

        """Write about AI agents for deployment in the same punchy style.
TOPIC: AI agents handling deployments and DevOps
- Hook about AI doing deployments
- Reality check about production complexity
- Bullet points about monitoring, rollbacks, scaling
- 👉 points about DevOps skills still needed
- Question about AI handling production incidents
- Hashtags: #AIAgents #DevOps #Production #Deployment #Developers"""
    ]
    
    prompt = random.choice(prompts)
    
    try:
        response = model.generate_content(prompt)
        content = response.text.strip()
        
        # Remove problematic Unicode characters for Windows console
        content_clean = content.encode('ascii', 'ignore').decode('ascii')
        
        print("GENERATED POST:")
        print("=" * 60)
        print(content_clean)
        print("=" * 60)
        
        # Also save to file to see full content with emojis
        with open('generated_post.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Full post with emojis saved to: generated_post.txt")
        
        return content
        
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    test_style_generation()