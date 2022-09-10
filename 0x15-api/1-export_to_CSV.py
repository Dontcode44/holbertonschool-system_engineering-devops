#!/usr/bin/python3
"""Using the rest API"""

import csv
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

    with open("{}.csv".format(emp_id), 'w') as fi_csv:
        f_ile = fi_csv.writer(fi_csv, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in u_all:
            f_ile.writerow([emp_id, users.get('username'),
                            task.get('completed'), task.get('title')])
