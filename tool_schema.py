add_task_json = {
    "name": "add_task",
    "description": "Add a new task to the todo list",
    "parameters": {
        "type": "object",
        "properties": {
            "task": {
                "type": "string",
                "description": "Task to be added"
            }
        },
        "required": ["task"]
    }
}
list_tasks_json = {
    "name": "list_tasks",
    "description": "List all tasks",
    "parameters": {
        "type": "object",
        "properties": {}
    }
}
complete_task_json = {
    "name": "complete_task",
    "description": "Mark a task as completed",
    "parameters": {
        "type": "object",
        "properties": {
            "task_name": {
                "type": "string",
                "description": "Name of the task to mark as completed"
            }
        },
        "required": ["task_name"]
    }
}
delete_task_json = {
    "name": "delete_task",
    "description": "Delete a task from the todo list",
    "parameters": {
        "type": "object",
        "properties": {
            "task_name": {
                "type": "string",
                "description": "Name of the task to delete"
            }
        },
        "required": ["task_name"]
    }
}
tools = [
    {
        "type": "function",
        "function": add_task_json
    },
    {
        "type": "function",
        "function": list_tasks_json
    },
    {
        "type": "function",
        "function": complete_task_json
    },
    {
        "type": "function",
        "function": delete_task_json
    }
]