import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Instagram API
INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
INSTAGRAM_USER_ID = os.getenv("INSTAGRAM_USER_ID")

# Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Image Search API (e.g., Unsplash)
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
