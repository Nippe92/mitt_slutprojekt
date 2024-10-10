from datetime import datetime
import json

class ToDo:
    def __init__(self, task_name, status="undone"):
        self.task_name = task_name
        self.status = status
        self.time_created = datetime.now()  # Sätter en tidstämpel när uppgiften skapas
        self.completion_time = None  # Sätter tidstämpel när uppgift är klar med None som huvudstatus.

    def done_Tasks(self):
        self.status = "Completed"
        self.completion_time = datetime.now()  # Sätter tid när uppgiften markeras som klar

class Todo_list:
    def __init__(self):
        self.tasks = []  # Lista för att hålla uppgifterna

    def add_task(self, task_name):
        task = ToDo(task_name)
        self.tasks.append(task)

    def show_task(self):
        if not self.tasks:
            print("Inga uppgifter tillgängliga.")
        else:
            for index, task in enumerate(self.tasks, 1):
                status = f"[{task.status}]"
                time_created = task.time_created.strftime("%Y-%m-%d %H:%M:%S")
                completion_time = task.completion_time.strftime("%Y-%m-%d %H:%M:%S") if task.completion_time else "Ej klar"
                print(f"{index}. {task.task_name} {status}, Skapad: {time_created}, Klar: {completion_time}")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.done_Tasks()  # Använder rätt metod för att markera uppgiften som klar
            print(f"Uppgift '{task.task_name}' har markerats som klar.")
        else:
            print("Ogiltigt uppgiftsnummer.")

    def add_json(self):
        j_file = []
        for task in self.tasks:
            j_file.append({
                "task_name": task.task_name,
                "status": task.status,
                "time_created": task.time_created.strftime("%Y-%m-%d %H:%M:%S"),
                "completion_time": task.completion_time.strftime("%Y-%m-%d %H:%M:%S") if task.completion_time else None
            })
        with open("ToDoList.json", "w") as file:  # Använd "w" för att skriva om filen
            json.dump(j_file, file, indent=4)
        print("Uppgifterna har nu sparats till JSON.")

    def load_json(self, filename="ToDoList.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for item in data:
                    task = ToDo(item["task_name"], item["status"])
                    task.time_created = datetime.strptime(item["time_created"], "%Y-%m-%d %H:%M:%S")
                    if item["completion_time"]:
                        task.completion_time = datetime.strptime(item["completion_time"], "%Y-%m-%d %H:%M:%S")
                    self.tasks.append(task)
                print("Uppgifterna har laddats från JSON.")
        except FileNotFoundError:
            print("Ingen JSON-fil hittades, börjar med tom lista.")

def main():
    todo_list = Todo_list()
    todo_list.load_json()  # Ladda uppgifter från JSON-fil om den finns

    while True:
        print("\n1: Lägg till uppgift")
        print("2: Visa uppgifter")
        print("3: Uppdatera status")
        print("4: Spara och avsluta")
        val = input("Välj ett alternativ: ")

        if val == "1":
            task_name = input("Ange din uppgift: ")
            todo_list.add_task(task_name)
        elif val == "2":
            print("Här är dina uppgifter:")
            todo_list.show_task()
        elif val == "3":
            todo_list.show_task()
            task_index = int(input("Ange numret på uppgiften att markera som klar: ")) - 1
            todo_list.complete_task(task_index)
        elif val == "4":
            todo_list.add_json()  # Spara till JSON när programmet avslutas
            print("Programmet avslutas...")
            break
        else:
            print("Ogiltigt val, försök igen.")

main()



    


