from app.Story.story_schema import StoryRequest, StoryResponse
from app.Story.openai_service import OpenAIService

class StoryManager:
    def __init__(self):
        # Instantiate the OpenAI service client layer
        self.openai_service = OpenAIService()

    def create_story(self, request_data: StoryRequest) -> StoryResponse:
        """
        Takes validated request data, extracts parameters, and calls the OpenAI service.
        """
        # Call the OpenAI service using the validated parameters from our request schema
        story = self.openai_service.generate_structured_story(
            character_name=request_data.character_name,
            character_type=request_data.character_type,
            genre=request_data.genre
        )
        
        return story