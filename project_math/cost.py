
def compute_earned_value(budget_at_completion, percent_completion) -> int:

    if percent_completion > 1 or percent_completion < 0:
        raise ValueError('Percentage values must be provided in their decimal format. E.g. 45% is 0.45')

    return round(budget_at_completion * percent_completion)


def compute_planned_value(budget_at_completion, percent_planned_completion) -> int:

    if percent_planned_completion > 1 or percent_planned_completion < 0:
        raise ValueError('Percentage values must be provided in their decimal format. E.g. 45% is 0.45')

    return round(budget_at_completion * percent_planned_completion)


def compute_cost_variance(earned_value, actual_cost) -> int:
    return earned_value - actual_cost


def compute_schedule_variance(earned_value, planned_value) -> int:
    return earned_value - planned_value


def compute_cost_performance_index(earned_value, actual_cost) -> float:
    return round(earned_value / actual_cost, 2)


def compute_schedule_performance_index(earned_value, planned_value) -> float:
    return round(earned_value / planned_value, 2)


def compute_estimate_at_completion(budget_at_completion, cost_performance_index) -> int:

    if cost_performance_index > 1 or cost_performance_index < 0:
        raise ValueError('Index (CPI) values must be provided in their decimal format. E.g. 45% is 0.45')

    return budget_at_completion / cost_performance_index


def compute_estimate_to_complete(estimate_at_completion, actual_cost) -> int:
    return estimate_at_completion - actual_cost

