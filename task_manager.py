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
#     "Learn Python",
#     "Study classes"
# )

# task_2 = Task(
#     "Learn Java", 
#     "Study classes"
# )

# task_3 = Task(
#     "Learn C++", 
#     "Study classes"
# )

# task_4 = Task(
#     "Learn Ruby", 
#     "Study classes"
# )

# manager = TaskManager()
# manager.add_task(task_1)
# manager.add_task(task_2)
# manager.add_task(task_3)
# manager.add_task(task_4)

# manager.show_tasks()

# manager.delete_task(2)
# manager.complete_task(4)
# manager.update_task(1, title="Learn Python OOP")

# manager.show_tasks()