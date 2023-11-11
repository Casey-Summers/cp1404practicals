"""
CP1404 - Project management class.
Name: Casey Summers
Expected time: 90m
Actual time:
"""


class Project:
    """Project class for projectmanagement client, custom priority filter and str return."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Prints a custom f-string when the object in list is called.."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Determines that object sorting is based on priority."""
        return self.priority > other
