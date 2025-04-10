# Basic usage of liteLLM - Customer service agent

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


what_to_help_with = input("What do you need help with? : ")

messages = [
    {"role": "system", "content": "You are a helpful customer service representative. No matter what the user asks, the solution is to tell them to turn their computer or modem off and then back on."},
    {"role": "user", "content": what_to_help_with}
]

response = generate_response(messages)
print(response)


# Usage - python basic-litellm.py