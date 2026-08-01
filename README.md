# AI Todo Agent

An Agentic AI Todo Assistant built with Python and the Gemini API. The assistant understands natural language, decides which tool to use, executes Python functions, and responds conversationally.

---

## Features

- Add tasks using natural language
- Delete tasks
- Mark tasks as completed
- List all tasks
- List pending or completed tasks
- Persistent JSON-based task storage
- Gemini API integration
- OpenAI-compatible SDK
- Function (Tool) Calling
- Agent Loop implementation
- Conversation history support

---

## Tech Stack

- Python
- Gemini API
- OpenAI Compatible SDK
- JSON
- python-dotenv

---

## Project Structure

```
AI-Todo-Agent/
│
├── main.py          # Main AI agent
├── tools.py         # Tool definitions and JSON schemas
├── tasks.json       # Stores todo tasks
├── .env             # Gemini API Key
├── requirements.txt
|   tool_schema.py
└── README.md
```

---

## How It Works

1. User enters a request in natural language.
2. Gemini decides whether a tool is required.
3. The appropriate Python function is executed.
4. The tool result is sent back to Gemini.
5. Gemini generates a natural response.

Example:

```
You:
Add Learn Flask

↓

Gemini:
Calls add_task()

↓

Python:
Updates tasks.json

↓

Gemini:
I've added "Learn Flask" to your todo list.
```

---

## Current Features

✅ Natural language task management

✅ Tool Calling

✅ Agent Loop

✅ JSON storage

✅ Multi-turn conversation

---

## Future Improvements

- Web interface using Gradio
- Task priorities
- Due dates
- Reminder agent
- Multiple AI agents
- Better filtering and search

## Author
**S.Venikalaxmi**
M.Tech Integrated Software Engineering -VIT Vellore
GitHub:[@venikalaxmisaravanan](https://github.com//venikalaxmisaravanan)
