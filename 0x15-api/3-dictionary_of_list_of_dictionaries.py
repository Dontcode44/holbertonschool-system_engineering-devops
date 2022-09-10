#!/usr/bin/python3
"""Using the rest API"""

import json
import requests
import sys

if __name__ == "__main__":
    """
    Write a Python script that, using this REST API
    """
    emp_id = int(sys.argv[1])

    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(emp_id)).json()

    u_all = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(emp_id)).json()

    user_dict = {}
    usernamedict = {}
    for user in users:
        ID = user.get("id")
        user_dict[ID] = []
        usernamedict[ID] = user.get('username')
    for task in u_all:
        task_dict = {}
        ID = task.get("userId")
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict['username'] = usernamedict.get(ID)
        user_dict.get(ID).append(task_dict)
    with open("todo_all_employees.json", 'w') as jsfile:
        json.dump(user_dict, jsfile)
