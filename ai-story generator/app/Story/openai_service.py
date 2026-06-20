from openai import OpenAI
from app.core.config import settings
from app.Story.story_schema import StoryResponse
from app.utils.prompt_template import STORY_PROMPT_TEMPLATE

class OpenAIService:
    def __init__(self):
        # Initialize the OpenAI client using the central settings configuration
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.MODEL_NAME

    def generate_structured_story(self, character_name: str, character_type: str, genre: str) -> StoryResponse:
        """
        Sends the formatted prompt to OpenAI and forces a structured StoryResponse output.
        """
        # Format the prompt layout with the user's specific inputs
        user_prompt = STORY_PROMPT_TEMPLATE.format(
            character_name=character_name,
            character_type=character_type,
            genre=genre
        )

        try:
            # Request a structured completion from OpenAI
            completion = self.client.beta.chat.completions.parse(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a professional children's book author. Write engaging, creative, and moral-driven short stories."},
                    {"role": "user", "content": user_prompt}
                ],
                response_format=StoryResponse, # This enforces the exact JSON structure we want
                temperature=0.7
            )
            
            # Return the parsed, fully typed object
            return completion.choices[0].message.parsed

        except Exception as e:
            print(f"Error communicating with OpenAI: {e}")
            raise e