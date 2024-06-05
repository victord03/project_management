
class Activity:
    name: str
    activity_index: str
    duration: int
    is_critical: bool
    cost_per_day: int
    total_cost: int

    def __init__(self, name, duration, activity_index='', is_critical=False, cost_per_day=0):
        self.name = name
        self.duration = duration
        self.activity_index = activity_index
        self.is_critical = is_critical
        self.cost_per_day = cost_per_day
        self.total_cost = self.cost_per_day * duration

    def __str__(self):
        return f'<{self.activity_index}: `{self.name}`; Duration: {self.duration}; Is Critical: {self.is_critical}; Cost per day: {self.cost_per_day}; Total Cost: {self.total_cost}>'
