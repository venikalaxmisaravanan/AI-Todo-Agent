import json

TASKS_FILE = "tasks.json"


def load_tasks():
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    tasks = load_tasks()

    tasks.append({
        "task": task,
        "status": "Pending"
    })

    save_tasks(tasks)

    return f"Task '{task}' added successfully."
def list_tasks():
    tasks = load_tasks()

    if not tasks:
        return "No tasks found."

    output = ""

    for i, task in enumerate(tasks, start=1):
        output += f"{i}. {task['task']} - {task['status']}\n"

    return output
def complete_task(task_name):
    tasks = load_tasks()

    for task in tasks:
        if task["task"].lower() == task_name.lower():
            task["status"] = "Completed"
            save_tasks(tasks)
            return f"Task '{task_name}' marked as completed."

    return "Task not found."
def delete_task(task_name):
    tasks = load_tasks()

    updated_tasks = [
        task
        for task in tasks
        if task["task"].lower() != task_name.lower()
    ]

    save_tasks(updated_tasks)

    return f"Task '{task_name}' deleted."