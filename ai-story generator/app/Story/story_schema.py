from pydantic import BaseModel, Field
from typing import List

class StoryRequest(BaseModel):
    """
    Validates the user's incoming request parameters.
    """
    character_name: str = Field(..., description="The name of the main character.")
    character_type: str = Field(..., description="The type of character (e.g., astronaut, wizard, detective).")
    genre: str = Field(..., description="The genre of the story (e.g., sci-fi, fantasy, mystery).")

class StoryResponse(BaseModel):
    """
    Enforces a strict structured output format from the OpenAI API.
    """
    title: str = Field(..., description="A catchy title for the generated story.")
    moral: str = Field(..., description="The lesson or moral of the story.")
    story_paragraphs: List[str] = Field(..., description="The story broken down cleanly into sequential paragraphs.")