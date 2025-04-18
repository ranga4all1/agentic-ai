# Quasi agent - With memory/context
# To generate any Python function based on user input

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

# First prompt:
"""
- Ask the user what function they want to create
- Ask the LLM to write a basic Python function based on the user’s description
- Store the response for use in subsequent prompts
- Parse the response to separate the code from the commentary by the LLM
"""

what_to_help_with = input("What function you want to create? : ")

messages = [
   {"role": "system", "content": "You are an expert software engineer that prefers functional programming. Use Python unless otherwise specified."},
   {"role": "user", "content": what_to_help_with}
]

response1 = generate_response(messages)
print("response1:", response1)
print("=" * 50)

# Second prompt: including the previous response
# We are going to make this verbose so it is clear what
# is going on. In a real application, you would likely
# just append to the messages list.
"""
 - Pass the code generated from the first prompt
 - Ask the LLM to add comprehensive documentation including:
    - Function description
    - Parameter descriptions
    - Return value description
    - Example usage
    - Edge cases
"""

messages = [
   {"role": "system", "content": "You are an expert software engineer that prefers functional programming. Use Python unless otherwise specified."},
   {"role": "user", "content": what_to_help_with},
   
   # Here is the assistant's response from the previous step
   # with the code. This gives it "memory" of the previous
   # interaction.
   {"role": "assistant", "content": response1},
   
   # Now, we can ask the assistant with second prompt
   {"role": "user", "content": "Update the function to add comprehensive documentation including "
   "Function description, Parameter descriptions, Return value description, Example usage, Edge cases"}
]

response2 = generate_response(messages)
print("response2:", response2)
print("=" * 50)


# Third prompt: including the previous response
"""
- Ask the LLM to add test cases using Python’s unittest framework
- Tests should cover:
    - Basic functionality
    - Edge cases
    - Error cases
    - Various input scenarios
"""
messages = [
   {"role": "system", "content": "You are an expert software engineer that prefers functional programming. Use Python unless otherwise specified."},
   {"role": "user", "content": what_to_help_with},
   
   # Here is the assistant's response from the previous step
   # with the code. This gives it "memory" of the previous
   # interaction.
   {"role": "assistant", "content": response2},
   
   # Now, we can ask the assistant with second prompt
   {"role": "user", "content": "add test cases using Python’s unittest framework. "
   "Tests should cover: Basic functionality, Edge cases, Error cases, Various input scenarios"}
]

response3 = generate_response(messages)
print("response2:", response3)
print("=" * 50)


# Usage - python quasi-agent.py