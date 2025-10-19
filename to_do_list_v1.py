tasks = list()
title = "--To Do List--"


while True:
    print(title)
    print("1. Show tasks")
    print("2. Add tasks")
    print("3. Mark tasks as done")
    print("4. Del tasks")
    print("5. Exit")

    choice = int(input("choose your option (e.g 1): \n").strip())

    if choice == 1:
        if not tasks:
            print(title)
            print("your list is empty")
            print("\n")

        else:
            print(title)
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Done" if task["done"] else "Not done yet"
                print(f"{i}. {task["task"]} - {status},\n")

    elif choice == 2:
        print("Type your tasks one by one. Type 'X' to stop adding.\n")
        while True:
            new_task = input("Task: ").strip()
            if new_task.upper() == 'X':
                print("Stopped adding tasks.\n")
                break
            elif new_task:
                tasks.append({"task": new_task, "done": False})
                print("Task added!\n")
            else:
                print("Please type something or 'X' to stop.\n")

    elif choice == 3:
        if not tasks:
            print("No tasks to mark.\n")
            continue
        try:
            num = int(input("Enter task number to mark as done: ").strip())
            tasks[num - 1]["done"] = True
            print("Task marked as done!\n")
        except (ValueError, IndexError):
            print("Invalid task number.\n")

    elif choice == 4:
        if not tasks:
            print("No tasks to delete.\n")
            continue
        try:
            num = int(input("Enter task number to delete: ").strip())
            tasks.pop(num - 1)
            print("Task deleted successfully!\n")
        except (ValueError, IndexError):
            print("Invalid task number.\n")

    elif choice == 5:
        print("Goodbye!\n")
        break

    else:
        print("Invalid Choice\n")
    
# -----------------------------------------------------------------------------------    