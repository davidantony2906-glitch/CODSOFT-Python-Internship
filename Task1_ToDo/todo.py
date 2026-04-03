def get_todos():
    try:
        with open("todos.txt", "r") as f:
            return f.readlines()
    except:
        return []

def write_todos(todos):
    with open("todos.txt", "w") as f:
        f.writelines(todos)

todos = get_todos()

while True:
    user = input("Enter ADD, SHOW, EDIT, COMPLETE, EXIT: ").strip().lower()

    match user:
        case "add":
            todo = input("Enter task: ").capitalize() + "\n"
            todos.append(todo)
            write_todos(todos)

        case "show":
            if not todos:
                print("No tasks found")
            else:
                for i, t in enumerate(todos):
                    print(f"{i+1}. {t.strip()}")                  
        case "edit":
            try:
                num = int(input("Task number to edit: ")) - 1
                new = input("Enter new task: ").capitalize() + "\n"
                todos[num] = new
                write_todos(todos)
            except:
                print("Invalid number")

        case "complete":
            try:
                num = int(input("Task number to remove: ")) - 1
                todos.pop(num)
                write_todos(todos)
            except:
                print("Invalid number")

        case "exit":
            print("Goodbye 👋")
            break

        case _:
            print("Invalid command")
