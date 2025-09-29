from gemini_linkedin import LinkedInGeminiBot
import os

def test_final_style():
    # Test content generation only
    bot = LinkedInGeminiBot()
    
    print("Testing your exact style for AI agent posts...")
    print("=" * 60)
    
    # Generate 3 different posts to see variety
    for i in range(3):
        print(f"\nPOST {i+1}:")
        print("-" * 40)
        content = bot.generate_content()
        
        # Clean for console display
        content_clean = content.encode('ascii', 'ignore').decode('ascii')
        print(content_clean)
        
        # Save full version
        with open(f'style_test_{i+1}.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Full version saved to: style_test_{i+1}.txt")
        print("-" * 40)

if __name__ == "__main__":
    test_final_style()