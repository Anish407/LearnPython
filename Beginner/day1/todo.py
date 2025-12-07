import requests

def get_all_todos():
    response = requests.get("https://jsonplaceholder.typicode.com/todos", timeout=10)
    response.raise_for_status()  # throws if not 2xx
    return response.json()

def get_todo_for_user(userId, todo):
    #user_todos= [todo for todo in todos if todo['userId'] == userId]
    if todo["userId"] == userId:
     return todo
    else:
        return None

def get_user_input():
    try:
        user_input= int(input("Enter a user ID: "))
        return user_input
    except ValueError:
        print("Invalid input. Please enter a valid integer user ID.")
        return get_user_input()
 

userId= int(input("Enter a user ID (1-10): "))
todos= get_all_todos()
pending_tasks=0
completed_tasks=0
total_todos=0
pending_todos=[]

for todo in todos:
    user_todo= get_todo_for_user(userId, todo)
    if user_todo:
        if todo.get("completed"):
            completed_tasks += 1
        else:
            pending_tasks += 1
            pending_todos.append(user_todo)
        total_todos += 1

print("_________Todo summary__________")        
print(f"Total todos for user {userId}: {total_todos}")
print(f"Completed todos for user {userId}: {completed_tasks}")

print(f"_________Pending todos = {pending_tasks}  for user {userId} __________")        
for total_todo in pending_todos:
    print(f"- {total_todo['title']}")
