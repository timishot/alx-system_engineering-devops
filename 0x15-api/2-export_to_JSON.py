#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress."""
import json
import requests
import sys


def export_todo_list_to_json(employee_id):
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

        json_data = {str(employee_id): [{"task": task["title"], "completed":
                     str(task['completed']), "username": user_data['username']}
                     for task in todo_data]}

        json_file_path = f"{employee_id}.json"
        with open(json_file_path, "w") as jsonfile:
            json.dump(json_data, jsonfile)
        print(f'Data exported to {json_file_path} successfully.')
    except requests.exceptions.RequestException as e:
        print(f"Error fetched data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    export_todo_list_to_json(employee_id)
