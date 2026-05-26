# Task Tracker CLI 

A simple command-line Task Tracker built using Python.  
It allows users to add, view, update, and delete tasks with persistent JSON storage.

---

## Features

1. Add new tasks with title, description, and due date
2. View all tasks sorted by due date
3. Mark tasks as completed
4. Delete tasks by ID
5. Persistent storage using JSON file
6. Input validation for safe usage

---

## Tech Stack

- Python 3
- JSON (for data storage)
- datetime module (for date validation & sorting)

---

## Project Structure
```
task-tracker/
│
├── main.py
├── task_manager.py
├── storage.py
├── tasks.json
└── README.md
```

---

##  How to Run

### 1. Clone the project
```bash
git clone https://github.com/VivekAggarwal07/task_tracker
cd task-tracker 
```
### 2. Run the program
```bash
python main.py
```
