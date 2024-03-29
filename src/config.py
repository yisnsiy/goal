# config class
from datetime import date


# this pricture's resolution is 1:2.2 (270:585)
class MyConfig():
    projects = {
        "Diet" : {
            'project': 'Diet',
            'left_picture': 'under_weight.png',
            'right_picture': 'health.png',
            'start_time': date(2024, 2, 18),
            'end_time': date(2024, 12, 30),
            'start_value': 55,
            'current_value': 60,
            'target_value': 65,
            'metric': 'Weight',
            'unit': 'kg'
        },
        "Sport": {
            'project': 'Sport',
            'left_picture': 'flat_body.png',
            'right_picture': 'muscles.png',
            'start_time': date(2024, 2, 18),
            'end_time': date(2024, 12, 30),
            'start_value': 15,
            'current_value': 13.4,
            'target_value': 12,
            'metric': 'Body Fat',
            'unit': '%'
        },
        "Read": {
            'project': 'Read',
            'left_picture': 'phone_addiction_cut.png',
            'right_picture': 'read.png',
            'start_time': date(2024, 2, 18),
            'end_time': date(2024, 12, 30),
            'start_value': 0,
            'current_value': 3,
            'target_value': 24,
            'metric': 'Amount',
            'unit': ' Books'
        }
    }