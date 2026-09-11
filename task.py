class Task:

    def __init__(self, title, description):
        self.id = 0
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True