#!/usr/bin/python3
"""Using the rest API"""

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

    results = []
    for i in u_all:
        if i.get('completed') is True:
            results.append(i.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(users.get('name'), len(results), len(u_all)))
    for i in results:
        print("\t {}".format(i))
