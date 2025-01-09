
import json


class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority):
        task = {
            'title': title,
            'description': description,
            'due_date': due_date,
            'priority': priority,
            'completed': False
        }
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def list_tasks_formatted(self):
        if not self.tasks:
            return "No tasks available."
        return "Tasks:\n" + "\n".join([f"- {task['title']} (Completed: {task['completed']})" for task in self.tasks])

    def mark_completed(self, title):
        for task in self.tasks:
            if task['title'] == title:
                task['completed'] = True

    def clear_tasks(self):
        self.tasks = []

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task['title'] != title]

    def edit_task(self, title, new_title=None, new_description=None, new_due_date=None, new_priority=None):
        for task in self.tasks:
            if task['title'] == title:
                if new_title:
                    task['title'] = new_title
                if new_description:
                    task['description'] = new_description
                if new_due_date:
                    task['due_date'] = new_due_date
                if new_priority:
                    task['priority'] = new_priority


if __name__ == "__main__":
    manager = ToDoListManager()
    manager.add_task("Estudiar Python", "Repasar clases y ejercicios", "2024-09-10", "Alta")
    print(manager.list_tasks_formatted())
