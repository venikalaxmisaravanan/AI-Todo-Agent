import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from tools import (
    add_task,
    delete_task,
    complete_task,
    list_tasks,
    tools
)

# -------------------------------------------------
# 1. Load API Key
# -------------------------------------------------

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# -------------------------------------------------
# 2. System Prompt
# -------------------------------------------------

system_prompt = """
You are an AI Todo Assistant.

Your job is to help users manage their todo list.

Whenever the user asks to:
- add a task
- delete a task
- complete a task
- list tasks

Use the available tools instead of pretending you did it yourself.
"""

# -------------------------------------------------
# 3. Tool Mapping
# -------------------------------------------------

tool_functions = {
    "add_task": add_task,
    "delete_task": delete_task,
    "complete_task": complete_task,
    "list_tasks": list_tasks
}

# -------------------------------------------------
# 4. Conversation History
# -------------------------------------------------

messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]

# -------------------------------------------------
# 5. Main Chat Loop
# -------------------------------------------------

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user
    })

    response = client.chat.completions.create(
        model="models/gemini-flash-latest",
        messages=messages,
        tools=tools
    )

    if response.choices[0].finish_reason == "tool_calls":

        message = response.choices[0].message

        messages.append(message)

        for tool_call in message.tool_calls:

            print("\nGemini wants to call a tool!")

            print("Tool Name :", tool_call.function.name)

            print("Arguments :", tool_call.function.arguments)

    else:

        reply = response.choices[0].message.content

        print("\nAssistant:", reply)

        messages.append({
            "role": "assistant",
            "content": reply
        })