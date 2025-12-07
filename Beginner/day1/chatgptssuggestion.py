import requests


def get_all_todos():
    response = requests.get("https://jsonplaceholder.typicode.com/todos", timeout=10)
    response.raise_for_status()
    return response.json()


def get_todos_for_user(todos, user_id):
    return [todo for todo in todos if todo.get("userId") == user_id]


def summarize_todos(user_todos):
    total = len(user_todos)
    completed = sum(1 for t in user_todos if t.get("completed"))
    pending = total - completed
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
    }


def main():
    try:
        user_id = int(input("Enter a user ID (1-10): "))
    except ValueError:
        print("Please enter a valid integer user ID.")
        return

    todos = get_all_todos()
    user_todos = get_todos_for_user(todos, user_id)

    if not user_todos:
        print(f"No todos found for user {user_id}.")
        return

    summary = summarize_todos(user_todos)

    print("_________Todo summary__________")
    print(f"Total todos for user {user_id}: {summary['total']}")
    print(f"Completed todos for user {user_id}: {summary['completed']}")
    print(f"Pending todos for user {user_id}: {summary['pending']}")

    if summary["pending"]:
        print(f"_________Pending todos ({summary['pending']}) for user {user_id} __________")
        for todo in user_todos:
            if not todo.get("completed"):
                print(f"- {todo['title']}")


if __name__ == "__main__":
    main()
