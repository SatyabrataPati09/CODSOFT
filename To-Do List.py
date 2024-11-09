# To-Do List Application

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark task as completed")
    print("4. Remove a task")
    print("5. Exit")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Incomplete"
            print(f"{index}. {task['task']} [{status}]")

# Function to add a new task
def add_task(tasks):
    new_task = input("\nEnter the new task: ")
    tasks.append({"task": new_task, "completed": False})
    print(f"Task '{new_task}' added to your to-do list.")

# Function to mark a task as completed
def mark_completed(tasks):
    try:
        task_number = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task '{tasks[task_number - 1]['task']}' marked as completed.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Please enter a valid task number.")

# Function to remove a task
def remove_task(tasks):
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' removed from your to-do list.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Please enter a valid task number.")

# Main function to run the application
def todo_list_app():
    tasks = []
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("\nThank you for using the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-5).")

# Run the application
todo_list_app()