import os
import json

file_path = "tasks.json"

def load_task():
    if os.path.exists(file_path):
        with open(file_path,"r") as file:
            return json.load(file)
    return []

def save_task(tasks):
    with open(file_path,"w") as file:
        json.dump(tasks,file,indent = 4)