from task import Task

class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for task in self.tasks:
            print(f"ID: {task.id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Completed: {task.completed}")
            print()

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

# manager.show_tasks()