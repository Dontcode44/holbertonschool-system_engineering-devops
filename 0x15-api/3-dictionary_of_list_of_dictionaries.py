#!/usr/bin/python3
"""Using the rest API"""

import json
import requests
import sys

if __name__ == "__main__":
    """
    Write a Python script that, using this REST API
    """
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos",
                        verify=False).json()
    u_dict = {}
    user_dict = {}
    for user in users:
        ID = user.get("id")
        u_dict[ID] = []
        user_dict[ID] = user.get('username')
    for task in todo:
        task_dict = {}
        ID = task.get("userId")
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict['username'] = user_dict.get(ID)
        u_dict.get(ID).append(task_dict)
    with open("todo_all_employees.json", 'w') as jsfile:
        json.dump(u_dict, jsfile)
