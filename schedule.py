
"""
Schedule
"""

import json
import arrow
from tabulate import tabulate


def sortSchedule(schedule):
    """ Sorts the schedule by time
    """
    output = []

    # Modified version of https://stackoverflow.com/a/11964572
    while schedule:
        minimum = schedule[0]  # arbitrary number in list

        for x in schedule:
            if x['timestamp'] < minimum['timestamp']:
                minimum = x

        output.append(minimum)
        schedule.remove(minimum)

    return output


def processSchedule(depth=5):
    """ Processes the "schedule.json" by sorting and merging them.
    """
    output = []

    with open('schedule.json', 'r') as file:
        schedule = json.loads(file.read())

    # Concatenate the output with the programs according to depth.
    for key in schedule:
        output += schedule[key][0:depth]

    return sortSchedule(output)


def viewSchedule():
    """ Views the processed schedule
    """
    processedSchedule = processSchedule()

    for x in processedSchedule:
        x.pop('timestamp')

    print(tabulate(processedSchedule, headers={
        'name': 'Name',
        'channel': 'Channel',
        'ETA': 'ETA',
        'showtime': 'Showtime (GMT+9)'
        }, tablefmt='psql'))


viewSchedule()
