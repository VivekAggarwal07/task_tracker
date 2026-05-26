from storage import load_task, save_task
from datetime import datetime

file_path = "tasks.json"

def add_task(title,desc,due_date):
    tasks = load_task() # loading existing tasks 
    task = {
        "id": generate_task_id(tasks),
        "title": title,
        "description": desc,
        "due_date": due_date,
        "status": "pending"
    }
    tasks.append(task) # adding the new task to the list of existing tasks
    save_task(tasks)
    return

def generate_task_id(tasks):
    if not tasks:
        return 1
    else:
        return max(task["id"] for task in tasks) + 1 # generating a unique ID

def view_tasks():
    return load_task()


def mark_complete(task_id):
    tasks = load_task()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed" # marking the task as completed
            save_task(tasks)
            return True
    return False

def delete_task(task_id):
    tasks = load_task()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task) # removing the task from the list
            save_task(tasks)
            return True
    return False
    
def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d") 
        return True
    except ValueError:
        return False

def sort_tasks_by_due_date():
    tasks = load_task()
    tasks.sort(key=lambda x: x["due_date"])
    return tasks