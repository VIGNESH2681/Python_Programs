# Initialize an empty to-do list
todo_list = []


# Function to add a task to the to-do list
def add_task():
    task = input("Enter a task to add: ")
    todo_list.append(task)
    print(f"Task '{task}' has been added to the to-do list.")


# Function to list all tasks in the to-do list
def list_tasks():
    if todo_list:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")


# Function to remove a task from the to-do list
def remove_task():
    list_tasks()
    if todo_list:
        task_index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_index < len(todo_list):
            removed_task = todo_list.pop(task_index)
            print(f"Task '{removed_task}' has been removed from the to-do list.")
        else:
            print("Invalid task number.")
    else:
        print("Your to-do list is empty.")


# Main program
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")