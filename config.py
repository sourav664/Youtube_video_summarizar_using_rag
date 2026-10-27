"""Configuration settings."""


# Model settings
LLM_MODEL = "gpt-4o-mini"

# =============================================================================
EMBEDDING_MODEL = "text-embedding-3-small"

# ProxyCurl API settings
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

API_KEY = api_key  # Replace with your API key
