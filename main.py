import os
from dotenv import load_dotenv

\# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")
    


def main():
    print("Hello from llm!")


if __name__ == "__main__":
    main()
