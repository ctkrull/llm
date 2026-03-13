import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


def main():
    prompt = args.user_prompt
    response = client.models.generate_content(model='gemini-2.5-flash', contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))
    p_tokens = response.usage_metadata.prompt_token_count
    r_tokens = response.usage_metadata.candidates_token_count
    
    if p_tokens is None or r_tokens is None:
        raise RuntimeError("Token count information is missing in the response metadata.")
    
    if args.verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {p_tokens}")  
        print(f"Response tokens: {r_tokens}")
        print(f"Response: \n{response.text}")
    
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")

    else:
        print(f"{response.text}")
        
if __name__ == "__main__":
    main()