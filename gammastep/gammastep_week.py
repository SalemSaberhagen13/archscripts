#!/usr/bin/env python
import datetime
import os

gamma_manager = '/home/salem/.local/bin/gammastep/gammastep_manager.sh'

def is_weekend_config_time():
    now = datetime.datetime.now()
    weekday = now.weekday()
    current_time = now.time()
    # Friday after 8am
    if weekday == 4 and current_time >= datetime.time(8, 0):
        return True
    # Saturday
    elif weekday == 5:
        return True
    # Sunday before 8am
    elif weekday == 6 and current_time < datetime.time(8, 0):
        return True
    return False

if is_weekend_config_time():
    os.system(f'{gamma_manager} movie')
else:
    os.system(gamma_manager)
