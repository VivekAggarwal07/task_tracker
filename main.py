from task_manager import add_task, mark_complete, delete_task, validate_date, sort_tasks_by_due_date

def display_menu():
    print("\nTask Tracker")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Status")
    print("4. Delete task")
    print("5. Exit")

def main():

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':

            while True:
                title = input("Enter a task: ").strip()

                if title:
                      break
                print("Task title cannot be empty.")

            desc = input("Enter a description: ")

            while True:
                due_date = input("Enter a due date (YYYY-MM-DD): ")

                if validate_date(due_date):
                    break
                print("Invalid date format. Please use YYYY-MM-DD.")
            add_task(title,desc,due_date)
            print("Task added successfully!")
        
        elif choice == '2':
            tasks = sort_tasks_by_due_date()
            print("\nTasks(Sorted by due date):")
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    print(f"ID: {task['id']}")
                    print(f"Title: {task['title']}")
                    print(f"Description: {task['description']}")
                    print(f"Due Date: {task['due_date']}")
                    print(f"Status: {task['status']}")
                    print("-" * 20)

        elif choice == "3":
            try:
                task_id = int(input("Enter the ID of the task to update: "))
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
                continue
            result = mark_complete(task_id)
            if result:
                print("Task marked as completed!")
            else:
                print("Task not found.")

        
        elif choice == "4":
            try:
                task_id = int(input("Enter the ID of the task to delete: "))
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
                continue
            result = delete_task(task_id)
            if result:
                print("Task deleted successfully!")
            else:
                print("Task not found.")

        elif choice == '5':
            print("Thank you for using the Task Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()