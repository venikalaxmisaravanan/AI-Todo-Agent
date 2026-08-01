from tools import add_task, list_tasks, complete_task, delete_task

while True:
    print("\n===== AI Todo Agent =====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        task = input("Enter task: ")
        print(add_task(task))

    elif choice == "2":
        print("\nTasks:")
        print(list_tasks())

    elif choice == "3":
        task = input("Enter completed task name: ")
        print(complete_task(task))

    elif choice == "4":
        task = input("Enter task to delete: ")
        print(delete_task(task))

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")