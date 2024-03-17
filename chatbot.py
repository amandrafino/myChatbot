# myChatBot.py
import os
from openai import OpenAI

# Fetch the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

# Instantiate the OpenAI client with the API key from the environment variable
client = OpenAI(api_key=api_key)

def get_completion(prompt):
    """Fetch a completion from OpenAI based on the given prompt."""
    try:
        # Updated to use the recommended replacement model: gpt-3.5-turbo-instruct
        completion = client.completions.create(
            model='gpt-3.5-turbo-instruct',  # Updated model
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )
        return completion.choices[0].text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
#if __name__ == "__main__":
#    test_prompt = "What is the capital of France?"
#    response = get_completion(test_prompt)
#    print(f"Response from OpenAI: {response}")


# Example usage with a loop
if __name__ == "__main__":
    while True:
        user_prompt = input("Ask me anything (type 'exit' to stop): ")
        if user_prompt.lower() == 'exit':
            print("Exiting. Have a great day!")
            break
        response = get_completion(user_prompt)
        print(f"Response from OpenAI: {response}")
