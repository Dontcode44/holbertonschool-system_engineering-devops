#!/usr/bin/python3
"""Using the rest API"""

import requests

if __name__ == "__main__":
    """
    Write a Python script that, using this REST API
    """
    from sys import argv
    employee_id = int(argv[1])

    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                      .format(employee_id)).json()

    u_all = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(employee_id)).json()

    results = []
    for i in u_all:
        if i.get('completed') is True:
            results.append(i.get('title'))
    print("Employee {} is done with results({}/{}):".
          format(users.get('name'), len(results), len(u_all)))
    for i in results:
        print("\t {}".format(i))
