import google.generativeai as genai
import os
from dotenv import load_dotenv
import random

def generate_perfect_style():
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Perfect style matching your example
    prompt = """Write a LinkedIn post EXACTLY in this style and format:

EXACT STYLE TO COPY:
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

NOW WRITE ABOUT: AI agents for automated testing

REQUIREMENTS:
1. Start with catchy hook like "AI testing sounds amazing… until reality hits."
2. One line about what AI agents promise in testing
3. "But here's the hard truth 👇"
4. "It's not just about [simple thing]. It's about:" 
5. 3 bullet points with emojis about real testing challenges
6. "This is why I keep saying:"
7. 2 points with 👉 about testing evolution
8. Paragraph about using AI but knowing fundamentals
9. "So yes, use AI agents. But also learn [skill]."
10. "That's where the real future of [role] lies 🚀"
11. Question about AI vs humans in testing
12. Hashtags: #AIAgents #Testing #QualityAssurance #FutureOfWork #Developers

KEEP IT PUNCHY, SHORT LINES, EXACTLY LIKE THE EXAMPLE!"""
    
    try:
        response = model.generate_content(prompt)
        content = response.text.strip()
        
        # Save full version
        with open('perfect_post.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Print clean version
        content_clean = content.encode('ascii', 'ignore').decode('ascii')
        print("PERFECT STYLE POST:")
        print("=" * 60)
        print(content_clean)
        print("=" * 60)
        print("Full version saved to: perfect_post.txt")
        
        return content
        
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    generate_perfect_style()