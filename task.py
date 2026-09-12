class Task:

    def __init__(self, title, description):
        self.id = 0
        self.title = title
        self.description = description
        self.completed = False
        self.deadline = None

    def mark_completed(self):
        self.completed = True