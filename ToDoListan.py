from datetime import datetime
import json

class ToDo:
    def __init__(self, task_name, status):
        self.task_name = task_name
        self.status = status

class Todo_list(ToDo):
    def list_task(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def edit_task(self):
        pass

    def show_task(self):
        pass

    def remove_task(self):
        pass

    def complete_task(self):
        pass

    def clear_all(self):
        self.tasks.clear()


    


