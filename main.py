class Task:
    """This object represents a task including its name, priority and due date."""
    
    def __init__(self, name, priority, due_date):
        """Initialises task, checking attributes for validity. Name must be string, length 1 to 20. Priority must be integer, value 0 to 100. Date must be string, in format YYYY-MM-DD."""
        
        # Add name attribute
        if type(name) == str and len(name) > 0 and len(name) < 50:
            self.name = name
        else:
            raise ValueError("Name input must be a string with length 1 to 50.") # incorrect input
        
        # Add priority attribute
        if type(priority) == int and priority >= 0 and priority <= 100:
            self.priority = priority
        else:
            raise ValueError("Priority input must be an integer between 0 and 100 (inclusive)") # incorrect input
        
        # Add date attribute
        if (
            isinstance(due_date, str) and len(due_date) == 10 and
            due_date[4] == '-' and due_date[7] == '-' and
            2024 <= int(due_date[:4]) < 2100 and
            0 < int(due_date[5:7]) <= 12 and
            0 < int(due_date[8:]) <= 31
        ):
            self.due_date = due_date         
        else:
            raise ValueError('Date must be string, in format "YYYY-MM-DD"') # incorrect input

class TaskList:
    """This object is a list of tasks objects that can be used to find and remove the highest priority task and view tasks for completion. """
    
    def __init__(self, initial_name=None, initial_priority=None, initial_due_date=None):
        """Initialisation function takes an optional initial task for the first element of the list"""
        self.task_list = [] # to store list of Tasks
        if initial_name is not None and initial_priority is not None and initial_due_date is not None:
            self.task_list.append(Task(initial_name, initial_priority, initial_due_date)) # if user inputs initial item, add to list
    
    def add_new(self, name, priority, due_date):
        """Method adds new task to the list"""
        if any(task.priority == priority for task in self.task_list): # O(n) time
            raise ValueError("Priority already in list") # priority should be unique
        else:
            self.task_list.append(Task(name, priority, due_date)) # add Task element to task_list
    
    def display(self):
        """Method displays the tasks currently in the list"""
        sorted_array = self.sort() # sort task list
        print("Tasks sorted by priority (highest priority first):")
        for task in sorted_array: # print each task from sorted list
            print(f"Name: {task.name}, Priority: {task.priority}, Due Date: {task.due_date}")
    
    def sort(self):
        """Bubble Sort algorithm to sort tasks by priority (highest priority first)"""
        tasks = self.task_list
        n = len(tasks)

        # validate empty task list
        if n == 0:
            raise ValueError("No tasks to sort.")

        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                # Compare adjacent tasks by priority (higher priority should come first)
                if tasks[j].priority < tasks[j + 1].priority:
                    # Swap if the current task has lower priority
                    tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]
                    swapped = True
            # If no elements were swapped, the list is already sorted
            if not swapped:
                break
        return tasks
            
    def find_highest_priority(self):
        """Method finds the highest priority task"""
        return self.sort()[0] # sort function has highest priority element in first place
    
    def remove_by_priority(self, priority):
        """Method removes a task based on inputted priority"""
        if len(self.task_list) == 0: # validate empty task list
            raise ValueError("No tasks in list")
        for i in self.task_list:
            if i.priority == priority: # find item
                self.task_list.remove(i)
                return # now item removed, end loop
        raise ValueError("Priority inputted is not in task list.")

# Testing  
l = TaskList()
l.add_new("eat", 5, "2024-09-10")
l.add_new("make dinner", 2, "2024-09-12")
l.add_new("make list",3, "2024-09-11")
l.add_new("update list", 7, "2024-09-15")
l.add_new("check teams", 10, "2024-09-18")
l.add_new("submit assignment", 11, "2024-09-14")
l.add_new("clean desk", 1, "2024-09-20")
l.add_new("clean room", 9, "2024-09-23")

print(l.find_highest_priority().name)
l.remove_by_priority(1)
l.display()
