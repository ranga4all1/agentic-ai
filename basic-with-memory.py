# Basic usage of liteLLM - With memory/context

# pip install python-dotenv
# pip install litellm

import os
from dotenv import load_dotenv

from litellm import completion
from typing import List, Dict

# Load environment variables and set API key
load_dotenv()
os.getenv("OPENAI_API_KEY")


def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024
    )
    return response.choices[0].message.content


messages = [
   {"role": "system", "content": "You are an expert software engineer that prefers functional programming."},
   {"role": "user", "content": "Write a function to swap the keys and values in a dictionary."}
]

response1 = generate_response(messages)
print("response1:", response1)
print("=" * 50)

# Second query including the previous response
# We are going to make this verbose so it is clear what
# is going on. In a real application, you would likely
# just append to the messages list.
messages = [
   {"role": "system", "content": "You are an expert software engineer that prefers functional programming."},
   {"role": "user", "content": "Write a function to swap the keys and values in a dictionary."},
   
   # Here is the assistant's response from the previous step
   # with the code. This gives it "memory" of the previous
   # interaction.
   {"role": "assistant", "content": response1},
   
   # Now, we can ask the assistant to update the function
   {"role": "user", "content": "Update the function to include documentation."}
]

response2 = generate_response(messages)
print("response2:", response2)
print("=" * 50)

# Usage - python basic-wit-memory.py