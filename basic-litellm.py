# Basic usage of liteLLM

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

response = generate_response(messages)
print(response)


# Usage - python basic-litellm.py