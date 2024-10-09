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

    def add_json(self):
        for task in self.tasks:
            self.j_file.append({"name of task":self.task_name, 
                                "status of task":self.status, 
                                "created time":self.time_created.strftime("%Y-%m-%d %H:%M:%S"), 
                                "completion time":self.completion_time.strftime("%Y-%m-%d %H:%M:%S")})
            with open ("ToDoList.json", "a") as file:
                json.dump(self.j_file, file indent=4)
            print("Uppgifterna har nu lagts till")

    def load_json(self, filename="ToDOList.json"):
        try:
            with open ("ToDoList.json", "r") as file:
                j_file = json.load(file)
                for item in j_file:
                    task = ToDo(item["task name"], item["status"])
                    task.time_created.strftime(item["time created: "], "%Y-%m-%d %H:%M:%S")
                    if item["completion time "]:
                        task.completion_time = datetime.strptime(item["completion_time"], "%Y-%m-%d %H:%M:%S")
                        self.tasks.append(task)
                    print("Uppgifterna har lagts till. ")
        except FileNotFoundError:
            print("Du har angivit fel filnamn")
            


def main()
    todo_list = Todo_list()
    todo_list.load_json()

    while True:
        print("1: lägga till uppgifter\n")
        print("2: visa uppgifter\n")
        print("3: uppdatera status\n")
        print("4: spara och avsluta")
        val = input("Välj någon av ovan alternativ genom att skriva siffran. \n")

        if val == "1":
            input("ange din uppgift du vill lägga till: \n")
            todo_list.add_task(task_name)
        elif val == "2":
            print("Här är dina uppgifter: \n")
            todo_list.load_json("r")
        elif val == "3":
            input("Ange uppgiften du vill uppdatera status på: \n")
            todo_list.load_json()
            task_number


    


