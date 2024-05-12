
def view_tasks(tasks):
    print()
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")
    print()

def add_tasks(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    view_tasks(tasks)

def update_tasks(tasks):
    view_tasks(tasks)
    choice = int(input("Enter which task to update: "))
    task = input("Enter a task: ")
    for i in range(len(tasks)):
        if i == choice - 1:
            tasks[i] = task

def delete_tasks(tasks):
    view_tasks(tasks)
    choice = int(input("Enter which task you wish to delete: "))
    for i in range(len(tasks)):
        if i == choice - 1:
            del(tasks[i])
    view_tasks(tasks)