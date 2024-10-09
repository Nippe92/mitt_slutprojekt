from datetime import datetime
import json

class ToDo:
    def __init__(self, task_name, status="undone"):
        self.task_name = task_name
        self.status = status
        self.time_created = datetime.now() #Sätter en tidstämpel när uppgift skapas
        self.completion_time = None #sätter tidstämpel när uppgift är klar med None som huvudstatus.
        self.edit_time = datetime.now() # sätter tidstämpel när uppgift uppdateras.

    def done_Tasks(self):
        self.status = "Completed"
        self.completion_time = datetime.now()

class Todo_list(ToDo): 
    def list_task(self):
        self.tasks = [] #Lägger till uppgifterna.
        self.j_file = [] #Lägger till uppgifter i json fil

    def add_task(self, task_name):
        task = ToDo(task_name)
        self.tasks.append(task)
        for task in self.tasks:
            self.j_file.append(self.task_name, self.status, self.time_created, self.completion_time)
        

    def edit_task(self):
        with open ("ToDoList.json", "a") as file:
            file.write()

    def show_task(self):
        with open ("ToDoList.json", "r") as file:
            file.read()

    def remove_task(self):
        pass

    def complete_task(self):
        pass

    def clear_all(self):
            self.tasks.clear()
            self.j_file.clear()
            



    


