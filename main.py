from task import Task
from task_manager import TaskManager

manager = TaskManager()
program_working = True

while program_working:
    print("""
    ===== TASK PLANNER =====

        1. Add task
        2. Show all tasks
        3. Show completed tasks
        4. Show active tasks
        5. Complete task
        6. Update task
        7. Delete task
        0. Exit

    """)

    user_input = int(input("Enter number: "))
    
    if user_input == 1:
        print("-" * 40) 
        title = input("Enter the title: ")
        description = input("Enter the description: ")
        print("-" * 40) 
        
        new_task = Task(title, description)
        manager.add_task(new_task)
        print("Task added successfully.")

    elif user_input == 2:
        manager.show_tasks()

    elif user_input == 0:
        program_working = False