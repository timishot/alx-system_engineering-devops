#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress."""
import requests
import sys


def get_todo_list_progress(employee_id):
    """API URL for user information"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    """API URL for user's TODO list"""
    todo_url = f"https://jsonplaceholder.typicode.com/" \
               f"todos?userId={employee_id}"

    try:
        """Fetch user information"""
        user_response = requests.get(user_url)
        user_data = user_response.json()

        """ Fetch TODO list"""
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        """Calculate progress"""
        total_tasks = len(todo_data)
        completed_tasks = sum(task['completed'] for task in todo_data)

        """ Display information"""
        print(f"Employee {user_data['name']} is done with\
 tasks({completed_tasks}/{total_tasks}):")
        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetched data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)
