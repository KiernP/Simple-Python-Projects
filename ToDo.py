import json
import time
import uuid

# Load existing tasks
try:
    with open("todos.json", "r") as file:
        todo_list = json.load(file)
except FileNotFoundError:
    todo_list = []

# View tasks
def view_todo():
    if not todo_list:
        print("No tasks found.")
        return

    print("\nTodo List:")
    for i, task in enumerate(todo_list, start=1):
        completed = "Completed" if task["completed"] else "Pending"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(task["timestamp"]))
        print(f"{i}. [{completed}] {task['task']} (ID: {task['id']}, Created: {timestamp})")

# Add task
def save_todo():
    task_description = input("Enter the new task:\n")
    new_task = {
        "id": str(uuid.uuid4()),
        "task": task_description,
        "completed": False,
        "timestamp": time.time()
    }
    todo_list.append(new_task)
    save_json()
    print("Task added successfully!")

# Update task description
def update_todo():
    view_todo()
    try:
        index = int(input("Enter the number of the task to update: "))
        task = todo_list[index - 1]
        new_description = input(f"Enter new description for '{task['task']}': ")
        task["task"] = new_description
        save_json()
        print("Task updated successfully!")
    except (ValueError, IndexError):
        print("Invalid number.")

# Delete task
def delete_todo():
    view_todo()
    try:
        index = int(input("Enter the number of the task to delete: "))
        removed_task = todo_list.pop(index - 1)
        save_json()
        print(f'Task "{removed_task["task"]}" deleted.')
    except (ValueError, IndexError):
        print("Invalid number.")

# Mark task as completed/uncompleted
def mark_todo_completed():
    view_todo()
    try:
        index = int(input("Enter the number of the task to toggle completion: "))
        task = todo_list[index - 1]
        task["completed"] = not task["completed"]
        status = "completed" if task["completed"] else "not completed"
        save_json()
        print(f'Task "{task["task"]}" is now {status}.')
    except (ValueError, IndexError):
        print("Invalid number.")

# Save the list to JSON
def save_json():
    with open("todos.json", "w") as file:
        json.dump(todo_list, file, indent=4)

# Main menu
def main_menu():
    loop = True
    while loop:
        print("\nMain Menu")
        print("1. View Todos")
        print("2. Add Todos")
        print("3. Update Todos")
        print("4. Delete Todos")
        print("5. Mark Todo as Completed")
        print("6. Exit")

        choice = input("Select an action from the menu: ")

        if choice == '1':
            view_todo()
        elif choice == '2':
            save_todo()
        elif choice == '3':
            update_todo()
        elif choice == '4':
            delete_todo()
        elif choice == '5':
            mark_todo_completed()
        elif choice == '6':
            print("Exiting program...")
            loop = False
        else:
            print("Invalid choice, please try again.")

# Run the program
main_menu()
