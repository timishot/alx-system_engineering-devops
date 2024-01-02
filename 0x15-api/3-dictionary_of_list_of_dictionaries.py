#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress."""
import json
import requests
import sys


def export_todo_list_to_json():
    user_url = "https://jsonplaceholder.typicode.com/users"
    all_user_response = requests.get(user_url)

    if all_user_response.status_code == 200:
        all_users = all_user_response.json()
        all_data = {}
        for user_data in all_users:
            employee_id = user_data['id']
            user_url = f"https://jsonplaceholder.typicode.com/users"\
                f"/{employee_id}"

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

                user_tasks = [{"username": user_data['username'],
                              "task": task["title"],
                               "completed": task['completed']}
                              for task in todo_data]
                all_data[str(employee_id)] = user_tasks

                json_file_path = f"todo_all_employees.json"
                with open(json_file_path, "w") as jsonfile:
                    json.dump(all_data, jsonfile)

                print(f'Data exported to {json_file_path} successfully.')
            except requests.exceptions.RequestException as e:
                print(f"Error fetched data: {e}")
                sys.exit(1)


if __name__ == "__main__":
    export_todo_list_to_json()
