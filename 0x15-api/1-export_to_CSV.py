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
    file_csv = sys.argv[1] + '.csv'

    users = requests.get("https://jsonplaceholder.typicode.com/users"
                         ).json()

    u_all = requests.get("https://jsonplaceholder.typicode.com/todos"
                         ).json()

    with open(file_csv, mode='w') as csv_file:
        the_file = csv.writer(csv_file, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_ALL)
        for x in users:
            if emp_id == x.get("id"):
                user_name = (x.get("username"))
        for y in u_all:
            if y.get("userId") == emp_id:
                the_file.writerow([str(emp_id), user_name, y.get("completed"),
                                   y.get("title")])
