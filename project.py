import csv
import datetime

class TaskAssignmentSystem:
    def __init__(self, task_file='tasks.csv'):
        self.task_file = task_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        try:
            with open(self.task_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # skip empty rows
                        task_id, task_name, emp_id, emp_name, deadline, status = row
                        tasks.append({
                            'task_id': task_id,
                            'task_name': task_name,
                            'emp_id': emp_id,
                            'emp_name': emp_name,
                            'deadline': deadline,
                            'status': status
                        })
        except FileNotFoundError:
            print("Task file not found. Creating a new one.")
        return tasks

    def assign_task(self, task_id, task_name, emp_id, emp_name, deadline):
        # Add task to task list
        task = {
            'task_id': task_id,
            'task_name': task_name,
            'emp_id': emp_id,
            'emp_name': emp_name,
            'deadline': deadline,
            'status': 'Assigned'
        }
        self.tasks.append(task)
        
        # Save to CSV file
        with open(self.task_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([task_id, task_name, emp_id, emp_name, deadline, 'Assigned'])
        
        print(f"Task '{task_name}' assigned to {emp_name} with a deadline of {deadline}.")

    def update_task_status(self, task_id, status):
        task_found = False
        for task in self.tasks:
            if task['task_id'] == task_id:
                task['status'] = status
                task_found = True
                # Update the CSV file with the new status
                self.save_tasks()
                print(f"Task {task_id} status updated to {status}.")
                break
        
        if not task_found:
            print(f"Task with ID {task_id} not found.")

    def save_tasks(self):
        with open(self.task_file, 'w', newline='') as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task['task_id'], task['task_name'], task['emp_id'], task['emp_name'], task['deadline'], task['status']])

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nTask List:")
        for task in self.tasks:
            print(f"Task ID: {task['task_id']}, Task Name: {task['task_name']}, Assigned to: {task['emp_name']}, Deadline: {task['deadline']}, Status: {task['status']}")

    def view_tasks_by_employee(self, emp_id):
        employee_tasks = [task for task in self.tasks if task['emp_id'] == emp_id]
        if not employee_tasks:
            print(f"No tasks found for employee ID {emp_id}.")
            return
        print(f"\nTasks for Employee ID {emp_id}:")
        for task in employee_tasks:
            print(f"Task ID: {task['task_id']}, Task Name: {task['task_name']}, Deadline: {task['deadline']}, Status: {task['status']}")

def main():
    system = TaskAssignmentSystem()

    while True:
        print("\nTask Assignment and Tracking System")
        print("1. Assign Task")
        print("2. Update Task Status")
        print("3. View All Tasks")
        print("4. View Tasks by Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_id = input("Enter Task ID: ")
            task_name = input("Enter Task Name: ")
            emp_id = input("Enter Employee ID: ")
            emp_name = input("Enter Employee Name: ")
            deadline = input("Enter Deadline (YYYY-MM-DD): ")
            system.assign_task(task_id, task_name, emp_id, emp_name, deadline)

        elif choice == '2':
            task_id = input("Enter Task ID to update: ")
            status = input("Enter new status (Assigned/In Progress/Completed): ")
            system.update_task_status(task_id, status)

        elif choice == '3':
            system.view_tasks()

        elif choice == '4':
            emp_id = input("Enter Employee ID to view their tasks: ")
            system.view_tasks_by_employee(emp_id)

        elif choice == '5':
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
