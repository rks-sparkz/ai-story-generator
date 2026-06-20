import os
from dotenv import load_dotenv

# Load the variables from the .env file into the system's environment memory
load_dotenv()

class Settings:
    # Read the values, using default fallbacks if they aren't found
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-5-mini")

# Instantiate a single configuration object to share across our entire app
settings = Settings()