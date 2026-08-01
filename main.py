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

# =====================================================
# 1. Load Gemini API
# =====================================================

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# =====================================================
# 2. System Prompt
# =====================================================

system_prompt = """
You are an AI Todo Assistant.

Your job is to help users manage their todo list.

Whenever the user asks to:
- add a task
- delete a task
- complete a task
- list tasks

Always use the available tools.

After receiving the tool result, explain the result naturally to the user.
"""

# =====================================================
# 3. Map tool names to Python functions
# =====================================================

tool_functions = {
    "add_task": add_task,
    "delete_task": delete_task,
    "complete_task": complete_task,
    "list_tasks": list_tasks
}

# =====================================================
# 4. Conversation History
# =====================================================

messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]

# =====================================================
# 5. Chat Loop
# =====================================================

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": user
        }
    )

    response = client.chat.completions.create(
        model="models/gemini-flash-latest",
        messages=messages,
        tools=tools
    )

    # =================================================
    # Agent Loop
    # Keep executing until Gemini no longer asks for tools
    # =================================================

    while response.choices[0].finish_reason == "tool_calls":

        assistant_message = response.choices[0].message

        messages.append(assistant_message)

        for tool_call in assistant_message.tool_calls:

            tool_name = tool_call.function.name

            arguments = json.loads(tool_call.function.arguments)

            tool_function = tool_functions[tool_name]

            tool_result = tool_function(**arguments)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_result
                }
            )

        response = client.chat.completions.create(
            model="models/gemini-flash-latest",
            messages=messages,
            tools=tools
        )

    # =================================================
    # Final assistant response
    # =================================================

    reply = response.choices[0].message.content

    print("\nAssistant:", reply)

    messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )