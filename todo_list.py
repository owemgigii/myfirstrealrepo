
tasks = []

print("TO-DO LIST APP")

while True:
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")
    print("5. Delete a task")

    choice = input("Choose an option: ")

    if choice == "1":
       task = input("Enter a task: ").strip()

if task:
    tasks.append({"name": task, "done": False})
    print("Task added successfully!")
else:
    print("Task cannot be empty.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["done"] else "Pending"
                print(f"{i}. {task['name']} - {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks to complete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")

            try:
                number = int(input("Enter task number: "))

                if 1 <= number <= len(tasks):
                    tasks[number - 1]["done"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

      elif choice == "4":
        print("Goodbye!")
        break

    elif choice == "5":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")

            try:
                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print("Deleted:", removed["name"])
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")
