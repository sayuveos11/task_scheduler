from task import Task

class TaskManager:

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, task):
        task.id = self.next_id
        self.tasks.append(task)
        self.next_id += 1


    def show_tasks(self):
        for task in self.tasks:
            print("-" * 40) 
            print(f"ID: {task.id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Completed: {task.completed}")
            print("-" * 40) 
            print()

    def show_task(self, task):
        print("-" * 40) 
        print(f"ID: {task.id}")
        print(f"Title: {task.title}")
        print(f"Description: {task.description}")
        print(f"Completed: {task.completed}")
        print("-" * 40) 
        print()

    def show_completed_tasks(self):
        for task in self.tasks:
            if task.completed:
                self.show_task(task)

    def show_active_tasks(self):
        for task in self.tasks:
            if not task.completed:
                self.show_task(task)
    
    def find_task(self, task_id):
        for task in self.tasks:
            if task_id == task.id:
                return task

        raise ValueError("There is no task with that ID.")

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        task.mark_completed()

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        self.tasks.remove(task)

    def update_task(self, task_id, title=None, description=None):
        task = self.find_task(task_id)
        if title:
            task.title = title

        if description:
            task.description = description