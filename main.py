import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")

client = genai.Client(api_key=api_key)


def main():
    prompt = 'Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
    response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents=prompt
    ) 
    X = response.usage_metadata.prompt_token_count
    Y = response.usage_metadata.candidates_token_count
    if X is None or Y is None:
        raise RuntimeError("Token count information is missing in the response metadata.")
    
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {X}")  
    print(f"Response tokens: {Y}")
    print(f"Response: \n{response.text}")


if __name__ == "__main__":
    main()
