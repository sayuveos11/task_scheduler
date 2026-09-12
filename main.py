from task import Task
from task_manager import TaskManager
from datetime import datetime

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
        8. Set deadline
        9. Set priority
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

    elif user_input == 3:
        manager.show_completed_tasks()

    elif user_input == 4:
        manager.show_active_tasks()

    elif user_input == 5:
        task_id = int(input("Enter task`s id: "))
        manager.complete_task(task_id)
        print("Task set as complete")

    elif user_input == 6:
        task_id = int(input("Enter task`s id: "))

        title = input("Enter new title (leave empty to keep current): ")
        description = input("Enter new description (leave empty to keep current): ")

        manager.update_task(task_id, title, description)

    elif user_input == 7:
        task_id = int(input("Enter task`s id: "))
        manager.delete_task(task_id)
        print("Task was deleted")

    elif user_input == 8:
        task_id = int(input("Enter task`s id: "))
        deadline = datetime.strptime(input("Enter deadline (YYYY-MM-DD): "), "%Y-%m-%d")

        manager.set_deadline(task_id, deadline)
        print("Deadline was set")

    elif user_input == 9:
        task_id = int(input("Enter task`s id: "))
        priority = int(input("""
        Choose priority:
        1. Low
        2. Medium
        3. High

        
        """))   
        manager.set_priority(task_id, priority)

    elif user_input == 0:
        program_working = False