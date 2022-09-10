#!/usr/bin/python3
"""Using the rest API"""

import requests
import sys
import json

if __name__ == "__main__":
    """
    Write a Python script that, using this REST API
    """
    emp_id = int(sys.argv[1])

    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(emp_id)).json()

    u_all = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(emp_id)).json()

    nameUser = users.get('username')
    tasks = []
    for task in u_all:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = nameUser
        tasks.append(task_dict)
    json_file = {}
    json_file[emp_id] = tasks
    with open("{}.json".format(emp_id), 'w') as jsfile:
        json.dump(json_file, jsfile)
