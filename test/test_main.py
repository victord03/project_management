from src import main
from classes.Activity import Activity

activity = {
    'name': 'Code the activity class',
    'act_index': '1.1',
    'duration': 1,
    'is_critical': True,
    'cost_per_day': 0,
}

act_name = activity['name']
act_index = activity['act_index']
act_dur = activity['duration']
act_cp = activity['is_critical']
act_cpd = activity['cost_per_day']


class TestActivity:

    def test_class_instance(self):
        a = Activity(name=act_name, activity_index=act_index, duration=act_dur, is_critical=act_cp, cost_per_day=act_cpd)
        assert isinstance(a, Activity)

