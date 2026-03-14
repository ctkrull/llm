import os
import sys
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from functions.call_function import call_function, available_functions


def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables.")

    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    for _ in range(20):
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            )
        )

        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)

        if response.function_calls:
            function_responses = []
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, verbose=args.verbose)

                if not function_call_result.parts:
                    raise Exception("Function call response is missing parts.")
                if function_call_result.parts[0].function_response is None:
                    raise Exception("Function call response is missing function_response.")
                if function_call_result.parts[0].function_response.response is None:
                    raise Exception("Function call response is missing function_response.response.")

                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")

                function_responses.append(function_call_result.parts[0])

            messages.append(types.Content(role="user", parts=function_responses))

        else:
            print(f"Final response:\n{response.text}")
            return

    print("Reached maximum iterations (20).")
    sys.exit(1)


if __name__ == "__main__":
    main()