tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def show_tasks():
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def delete_task(index):
    try:
        removed = tasks.pop(index-1)
        print(f"Removed: {removed}")
    except:
        print("Invalid task number")

while True:
    print("\n1.Add 2.Show 3.Delete 4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_task(input("Enter task: "))
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task(int(input("Enter task number: ")))
    elif choice == "4":
        break
