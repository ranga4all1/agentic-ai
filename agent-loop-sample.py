# agent loop - sample
# This is a sample agent loop using Litellm and OpenAI API.
# This agent will be able to list files in a directory, read their content, and answer questions about them.

# pip install python-dotenv
# pip install litellm

import os
import json
from dotenv import load_dotenv

from litellm import completion
from typing import List, Dict

# Load environment variables and set API key
load_dotenv()
os.getenv("OPENAI_API_KEY")


def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(model="openai/gpt-4o", messages=messages, max_tokens=1024)
    return response.choices[0].message.content


# The Agent Loop
while iterations < max_iterations:

    # 1. Construct prompt: Combine agent rules with memory
    prompt = agent_rules + memory

    # 2. Generate response from LLM
    print("Agent thinking...")
    response = generate_response(prompt)
    print(f"Agent response: {response}")

    # 3. Parse response to determine action
    action = parse_action(response)

    result = "Action executed"

    if action["tool_name"] == "list_files":
        result = {"result": list_files()}
    elif action["tool_name"] == "read_file":
        result = {"result": read_file(action["args"]["file_name"])}
    elif action["tool_name"] == "error":
        result = {"error": action["args"]["message"]}
    elif action["tool_name"] == "terminate":
        print(action["args"]["message"])
        break
    else:
        result = {"error": "Unknown action: " + action["tool_name"]}

    print(f"Action result: {result}")

    # 5. Update memory with response and results
    memory.extend(
        [
            {"role": "assistant", "content": response},
            {"role": "user", "content": json.dumps(result)},
        ]
    )

    # 6. Check termination condition
    if action["tool_name"] == "terminate":
        break

    iterations += 1


agent_rules = [
    {
        "role": "system",
        "content": """
You are an AI agent that can perform tasks by using available tools.

Available tools:
- list_files() -> List[str]: List all files in the current directory.
- read_file(file_name: str) -> str: Read the content of a file.
- terminate(message: str): End the agent loop and print a summary to the user.

If a user asks about files, list them before reading.

Every response MUST have an action.
Respond in this format:

```action
{
    "tool_name": "insert tool_name",
    "args": {...fill in any required arguments here...}
}
""",
    }
]

memory = []
iterations = 0
max_iterations = 5


def list_files() -> List[str]:
    """List all files in the current directory."""
    return os.listdir(".")


def read_file(file_name: str) -> str:
    """Read the content of a file."""
    with open(file_name, "r") as file:
        return file.read()


def parse_action(response: str) -> Dict:
    """Parse the LLM response into a structured action dictionary."""
    try:
        response = extract_markdown_block(response, "action")
        response_json = json.loads(response)
        if "tool_name" in response_json and "args" in response_json:
            return response_json
        else:
            return {
                "tool_name": "error",
                "args": {"message": "You must respond with a JSON tool invocation."},
            }
    except json.JSONDecodeError:
        return {
            "tool_name": "error",
            "args": {
                "message": "Invalid JSON response. You must respond with a JSON tool invocation."
            },
        }

def extract_markdown_block(text: str, block_type: str) -> str:


# Note: The above code is a simplified example and may not work as-is.
# You will need to implement the actual parsing logic and error handling.
# Also, ensure that you have the necessary permissions to read files in the directory.
# The code assumes that the agent is running in a directory where it has permission to list and read files.
# The agent loop will continue until the maximum number of iterations is reached or the agent decides to terminate.
# Make sure to test the code in a safe environment where you can control the files and directories.
# The agent will print the results of its actions and any errors encountered.


# Example: If the user asks, “What files are in this directory?”, the memory might look like this:

memory = [
    {"role": "user", "content": "What files are in this directory?"},
    {
        "role": "assistant",
        "content": '```action\n{"tool_name":"list_files","args":{}}\n```',
    },
    {"role": "user", "content": '["file1.txt", "file2.txt"]'},
]

