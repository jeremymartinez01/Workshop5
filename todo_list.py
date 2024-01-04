class Task:
    def __init__(self, name, description, status='Incomplete'):
        self.name = name
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        new_task = Task(name, description)
        self.tasks.append(new_task)
        print(f"Task '{name}' added to the to-do list.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks in the to-do list:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task.name} - {task.description} - Status: {task.status}")
        return self.tasks

    def mark_task_completed(self, task_number):
        if task_number > 0 and task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.status = 'Completed'
            print(f"Task '{task.name}' marked as completed.")
        else:
            print("Invalid task number.")

    def clear_tasks(self):
        self.tasks = []
        print("All tasks cleared.")

    def get_task_by_name(self, name):
        for task in self.tasks:
            if task.name.lower() == name.lower():
                return task
        print(f"No task with name '{name}' found.")
        
    def remove_task_by_name(self, name):
        task = self.get_task_by_name(name)
        if task:
            self.tasks.remove(task)
            print(f"Task '{name}' removed from the to-do list.")

    def edit_task_description(self, name, new_description):
        task = self.get_task_by_name(name)
        if task:
            task.description = new_description
            print(f"Description of task '{name}' updated.")
        else:
            print(f"No task with name '{name}' found.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n======= To-Do List Manager =======")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear all tasks")
        print("5. Find and remove a task by name")
        print("6. Edit task description")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            todo_list.add_task(name, description)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            todo_list.list_tasks()
            task_number = int(input("Enter task number to mark as completed: "))
            todo_list.mark_task_completed(task_number)
        elif choice == '4':
            todo_list.clear_tasks()
        elif choice == '5':
            todo_list.list_tasks()
            name = input("Enter task name to remove: ")
            todo_list.remove_task_by_name(name)
        elif choice == '6':
            todo_list.list_tasks()
            name = input("Enter task name to edit description: ")
            new_description = input("Enter new description: ")
            todo_list.edit_task_description(name, new_description)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()