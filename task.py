class Task:

    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True