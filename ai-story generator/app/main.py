from app.Story.story_schema import StoryRequest
from app.Story.story import StoryManager

def main():
    print("🚀 Initializing AI Story Generator...")
    
    # 1. Instantiate our orchestrator manager
    manager = StoryManager()
    
    # 2. Mock a validated user request using our Pydantic schema
    mock_request = StoryRequest(
        character_name="Barnaby",
        character_type="Clockwork Mouse",
        genre="Steampunk Adventure"
    )
    
    print(f"📝 Generating a {mock_request.genre} story about {mock_request.character_name}...")
    
    try:
        # 3. Pass the data through the pipeline to OpenAI
        generated_story = manager.create_story(mock_request)
        
        # 4. Print out our beautifully structured results
        print("\n" + "="*40)
        print(f"🎬 TITLE: {generated_story.title}")
        print("="*40)
        
        print("\n📖 STORY:")
        for i, paragraph in enumerate(generated_story.story_paragraphs, 1):
            print(f"\n[Paragraph {i}]\n{paragraph}")
            
        print("\n" + "="*40)
        print(f"💡 MORAL: {generated_story.moral}")
        print("="*40 + "\n")
        
    except Exception as e:
        print(f"\n❌ Execution failed: {e}")
        print("💡 Note: This is expected if your OPENAI_API_KEY is still set to 'your_temporary_api_key_here'.")

if __name__ == "__main__":
    main()