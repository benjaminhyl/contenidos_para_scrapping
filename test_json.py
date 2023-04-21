import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# print(todos[9])

todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
top_number = top_users[0][1]
users = []
for u_id, tasks in top_users:
    if tasks == top_number:
        users.append(str(u_id))

max_users = " and ".join(users)

# s = "s" if len(users) > 1 else ""
# print(f"user{s} {max_users} completed {top_number} TODOs")

# Define a function to filter out completed TODOs 
# of users with max completed TODOS.
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

# test_filter = filter(lambda x: x["completed"] and str(x["userId"]) in users, todos)
# print(list(test_filter))

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)