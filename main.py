class Task:

    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_task(self):
        for task in self.tasks:
            print(f"ID: {task.id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Completed: {task.completed}")
            print()

    def find_task(self, id):
        for task in self.tasks:
            if id == task.id:
                return task

        raise ValueError("There is no task with that ID.")

    def complete_task(self, id):
        task = self.find_task(id)
        task.mark_completed()

    def delete_task(self, id):
        task = self.find_task(id)
        self.tasks.remove(task)

    def update_task(self, id, title=None, description=None):
        task = self.find_task(id)
        if title:
            task.title = title

        if description:
            task.description = description

# TEST

# task_1 = Task(
#     1, 
#     "Learn Python",
#     "Study classes"
# )

# task_2 = Task(
#     2, 
#     "Learn Java", 
#     "Study classes"
# )

# manager = TaskManager()
# manager.add_task(task_1)
# manager.add_task(task_2)

# manager.complete_task(2)
# manager.update_task(1, title="Learn Python OOP")

# manager.show_task()