from functions import view_tasks, add_tasks, update_tasks, delete_tasks

def selection(choice, tasks):
    if choice == 1:
        add_tasks(tasks)
    elif choice == 2:
        view_tasks(tasks)
    elif choice == 3:
        update_tasks(tasks)
    elif choice == 4:
        delete_tasks(tasks) 

def print_menu():
    print("""
To do list menu:
          
    1. Add tasks
    2. View tasks
    3. Update tasks
    4. Delete tasks
    5. Exit
    """)

def main():

    tasks = []
    while True:
        print_menu()
        choice = int(input("Select an option: "))

        if choice == 5:
            break

        selection(choice, tasks)

if __name__ == "__main__":
    main()