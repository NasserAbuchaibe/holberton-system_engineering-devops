#!/usr/bin/python3
"""Gather data from an API
"""
import requests
from sys import argv


def employee_data(usr_id):
    """Python script that, using this REST API, for a given employee ID,
        returns information about his/her TODO list progress.
    Args:
        usr_id (int): employee id
    """
    num_done_t = 0
    total_t = 0

    empl = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(usr_id))

    name = empl.json().get('name')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    list_completed = []
    for dict_emp in todos.json():
        if dict_emp.get('userId') == int(usr_id):
            total_t += 1
            if dict_emp.get('completed'):
                num_done_t += 1
                list_completed.append(dict_emp)

    print("Employee {} is done with tasks({}/{}):"
          .format(name, num_done_t, total_t))

    print('\n'.join(["\t " + task.get('title') for task in list_completed]))

if __name__ == ('__main__'):
    employee_data(argv[1])
