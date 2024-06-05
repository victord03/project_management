
class Project:
    name: str
    duration: int
    bac: int
    pv: int
    percent_complete: float
    activities: dict

    def __init__(self, name, duration, budget_at_completion=0, planned_value=0, percent_complete=0.0):
        self.name = name
        self.duration = duration
        self.bac = budget_at_completion
        self.pv = planned_value
        self.percent_complete = percent_complete
        self.activities = dict()

    def __str__(self):
        return f'<Project `{self.name}`; Duration: {self.duration}; BAC: {self.bac}, PV: {self.pv}, %Comp: {self.percent_complete}; Number of activities: {len(self.activities.keys())}>'

    def set_activities(self, activities):
        self.activities = activities
