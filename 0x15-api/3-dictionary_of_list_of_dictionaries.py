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
    al_l = {}

    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(emp_id)).json()

    u_all = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(emp_id)).json()

    for user in users:
        taskList = []
        for task in u_all:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        al_l[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(al_l, f)
