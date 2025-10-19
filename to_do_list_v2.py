tasks = list()
title = "--To Do List--"

print(title)
print("1. Show tasks")
print("2. Add tasks")
print("3. Mark tasks as done")
print("4. Del tasks")
print("5. Exit")


def show_task(tasks):
    if not tasks:
        print(title)
        print("Your list is Empty\n")
    
    else:
        print(title)
        print("Your tasks list:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not yet Done"
            print(f"{i}, {task['task']} - {status} \n")
    
def add_task(tasks):
    print("type your tasks one by one, else put 'X' to quit.")
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

def mark_task_done(tasks):
        if not tasks:
            print("No tasks to mark.\n")
            pass
        try:
                num = int(input("Enter task number to mark as done: ").strip())
                tasks[num - 1]["done"] = True
                print("Task marked as done!\n")
        except (ValueError, IndexError):
                print("Invalid task number.\n")

def del_task(tasks):
            if not tasks:
                print("No tasks to mark.\n")
                pass

            try:
                num = int(input("Enter task number to mark as done: ").strip())
                tasks.pop(num -1)
                print("Task marked as done!\n")
            except (ValueError, IndexError):
                print("Invalid task number.\n")

def main():
    while True:
        choice = int(input("choose your option (e.g 1): \n").strip())

        if choice == "1":
            show_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            del_task(tasks)
        elif choice == "5":
            break

if __name__ == "__main__":
    main()