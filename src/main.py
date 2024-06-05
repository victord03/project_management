from classes.Activity import Activity
from classes.Project import Project
from project_math import cost


def main():

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

    act1 = Activity(name=act_name, activity_index=act_index, duration=act_dur, is_critical=act_cp, cost_per_day=act_cpd)

    print(act1)

    project = {
        'name': 'Project Management Software',
        'duration': 30,
        'bac': 50,
        'pv': 1,
        'percent_completion': 0.10,
        'activities': dict(),
    }

    prj_name = project['name']
    prj_dur = project['duration']
    prj_bac = project['bac']
    prj_pv = project['pv']
    prj_percom = project['percent_completion']
    prj_acts = project['activities']

    prj1 = Project(name=prj_name, duration=prj_dur, budget_at_completion=prj_bac, planned_value=prj_pv, percent_complete=prj_percom)

    print(prj1)


if __name__ == '__main__':
    main()
