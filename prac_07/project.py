"""
CP1404 - Project management class.
Name: Casey Summers
Expected time: 90m
Actual time:
"""


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}--{self.start_date}--{self.priority}--{self.cost_estimate}--{self.completion_percentage}"
