from openai import OpenAI
from dotenv import load_dotenv
import os
import json

from tools import (
    add_task,
    list_tasks,
    complete_task,
    delete_task,
)

from tool_schema import tools
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
system_prompt = """
You are an AI Todo Assistant.

You help users manage their todo list.

Whenever appropriate,
use the available tools.

Never invent task data.

Always rely on the tools.
"""
messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": user
    })