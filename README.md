## Task Management System

**Project Overview**

This project is a simple task management system built in Python. It allows users to create, manage, and prioritize tasks based on their due dates and urgency. The system ensures that each task has a unique priority and provides functionalities to display tasks, find the highest priority task, and remove tasks by their priority.

**Features**

- Task Creation: Users can create new tasks with a name, priority, and due date.
- Priority Management: Ensures each task has a unique priority, preventing duplicates.
- Sorting: Tasks are sorted by priority using a bubble sort algorithm, allowing users to see the most important tasks first.
- Error Handling: Provides meaningful error messages for invalid inputs or operations.

**Class Descriptions**

*Task*

Represents an individual task with the following attributes:
- name: The name of the task (string, 1-50 characters).
- priority: An integer representing the task's urgency (0-100).
- due_date: The due date of the task in "YYYY-MM-DD" format.

*TaskList*

Manages a list of Task objects and includes methods to:
- add_new(name, priority, due_date): Adds a new task to the list.
- display(): Displays all tasks sorted by priority.
- find_highest_priority(): Returns the task with the highest priority.
- remove_by_priority(priority): Removes a task with the specified priority.

*Lessons Learned*

- Object-Oriented Programming: Improved understanding of OOP principles by creating classes and methods to encapsulate task functionality.
- Input Validation: Gained experience in validating user input to ensure data integrity and prevent runtime errors.
- Sorting Algorithms: Implemented a bubble sort algorithm to sort tasks by priority, reinforcing algorithmic thinking.
- Error Handling: Practiced raising and managing exceptions to provide user-friendly feedback during incorrect operations.

- Example Usage
```
# Create a TaskList instance
l = TaskList()

# Add tasks
l.add_new("Eat", 5, "2024-09-10")
l.add_new("Make dinner", 2, "2024-09-12")

# Display tasks
l.display()

# Find and remove the highest priority task
highest_task = l.find_highest_priority()
print(f"Highest Priority Task: {highest_task.name}")
l.remove_by_priority(highest_task.priority)

# Display updated task list
l.display()
```

**Error Handling**

The program incorporates various checks and raises errors for:

- Invalid task names or lengths.
- Duplicate priorities.
- Invalid due date formats.
- Attempting to sort or remove tasks from an empty list.

**Conclusion**

This task management system demonstrates basic data structures and algorithms while providing an efficient way to manage tasks. It is an excellent example of applying Python programming skills in a practical context.
