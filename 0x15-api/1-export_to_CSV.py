#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress."""
import csv
import requests
import sys


def export_todo_list_to_csv(employee_id):
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

        """Prepare data for CSV"""
        csv_file_path = f"{employee_id}.csv"

        """Write data to csv file"""
        with open(csv_file_path, "w", newline='') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todo_data:
                csv_row = [
                    employee_id,
                    user_data['username'],
                    str(task['completed']),
                    task['title']
                ]
                csv_writer.writerow(csv_row)

        print(f'Data exported to {csv_file_path} successfully.')
    except requests.exceptions.RequestException as e:
        print(f"Error fetched data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_todo_list_to_csv(employee_id)
