

def main_menu():

    # Prints the whole menu of the program to show the user the possible inputs
    # Every number corresponds to different functions in the main function 'todo_list_program'

    print("1. Add a new task")
    print("2. Mark a task as completed")
    print("3. View all tasks")
    print("4. Quit the program")

def add_task(todo_list):

    # Adds the task from the user input in todo_list if valid
    # Sets the task as not completed

    task_input = input("Type a task to add: ")

    if not task_input:
        print("Invalid input. Please enter a non-empty task.")
        return

    todo_list.append({'task': task_input, 'completed': False})
    print(f"{task_input.strip()} task successfully added!")


def mark_as_completed(todo_list):

    # Sets the task by index as completed
    # Checks if the index is valid

    print("===== Tasks =====")
    display_tasks(todo_list)

    index = int(input("Enter the index of the task to mark it as completed.")) - 1

    if 0 <= index < len(todo_list):
        todo_list[index]["completed"] = True
        print("Task marked as completed!")
    elif index == 0 and len(todo_list) == 0:
        print(f"There are no tasks. Please insert a task first!")
    else:
        print("Invalid index. Please enter a valid index.")



def display_tasks(todo_list):

    # Displays all of the tasks inserted by the user if any
    # Prints some additional messages depending on the quantity of the completed tasks

    print("===== Tasks =====")
    completed_tasks = 0
    completed_all = False
    for i, task in enumerate(todo_list):
        status = '[Completed]' if task ['completed'] else "[ ]"
        print(f"Index {i + 1}. {status} {task ['task']} ")
        if task['completed']:
            completed_tasks += 1

    if len(todo_list) >= 4 and not any(task['completed'] for task in todo_list):
        print("You sure have many tasks to do!")

    if completed_tasks > 0:
        if completed_tasks == len(todo_list):
            print(f"You have completed all of the tasks so far! Congratulations!")
            completed_all = True
        if not completed_all:
            print(f"Congratulations you have completed {completed_tasks} tasks so far!")


def todo_list_program():

    # The main function
    # Has the logic of all other functions in a simple while loop
    # Holds the main list needed for the functionallity of the functions and the completed tasks variable

    todo_list = []
    completed_tasks = 0

    while True:
        main_menu()

        user_choice = input("Please enter your choice (1-4):")
        if user_choice == "1":
            add_task(todo_list)
        elif user_choice == "2":
            mark_as_completed(todo_list)
            completed_tasks += 1
        elif user_choice == "3":
            display_tasks(todo_list)
        elif user_choice == "4":
            print("Exiting the program. Goodbye!")
            if completed_tasks > 0:
                print(f"You have completed {completed_tasks} tasks!")
            break
        else:
            print("Invalid choice. Please inser a number between 1-4.")


todo_list_program()  # Starts the whole program