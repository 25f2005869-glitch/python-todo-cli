# To-Do List CLI App

# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []

def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    # Add Task
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if tasks:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks found.")

    # Delete Task
    elif choice == "3":
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                num = int(input("Enter task number to delete: "))
                removed = tasks.pop(num - 1)

                with open("tasks.txt", "w") as file:
                    for task in tasks:
                        file.write(task + "\n")

                print(f"Task '{removed}' deleted.")
            except:
                print("Invalid task number.")
        else:
            print("No tasks to delete.")

    # Exit
    elif choice == "4":
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice. Try again.")
