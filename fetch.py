
""" Fetches schedule information from the specified website.
"""

import urllib.request
import urllib.parse
import json
import re
import arrow
from constants import (URL, SCHEDULE_TIMEZONE, LOCAL_TIMEZONE,
                       CHANNEL_EXCLUSIONS, WANTED_PROGRAMS)


def fetch():
    """ Fetches the schedule of the wanted programs.
    """

    # This is the form I see when I debugged the page.
    values = {
        'search_model': 'text',
        'af0rmelement': 'aformelement',
        'ftext': '',
        'submit': 'Cari'
    }
    schedule = {}

    for x in WANTED_PROGRAMS:

        values['ftext'] = x

        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')  # data should be bytes
        req = urllib.request.Request(URL, data)

        with urllib.request.urlopen(req) as response:
            page = response.read()

        schedule[x] = processResponse(page.decode('utf-8'))

    with open('schedule.json', 'w+') as file:
        file.write(json.dumps(schedule))


def processResponse(response):
    """ Processes the response
    """

    # Collects all the programs name
    names = re.findall(r'(?<=\srel="facebox">)[a-zA-Z:/.,0-9- ]+',
                       response)

    # Collects all the programs channel name
    channels = re.findall(
        r"(?<=<\/span>)[\w\s]+(?=<\/td>)",
        response)

    # Collects all the programs showtime
    showtimes = re.findall(r"(?<=<td class='text-muted'>)" +
                           r"\d+\/\w+\/\d+ \d{2}:\d{2}" +
                           r"(?=<\/td>)", response)

    output = []

    # Combines "names", "channels", and "showtimes"
    # list into a list of objects.
    for index, value in enumerate(names):

        # Converts the showtime to an Arrow instance,
        # then converts the timezone to the local one.
        showtime = arrow.get(showtimes[index], 'DD/MMM/YYYY HH:mm').replace(
            tzinfo=SCHEDULE_TIMEZONE
            ).to(LOCAL_TIMEZONE)

        # Checks if the channel name is in the exclusion
        # list by comparing case insensitively.
        if any(x in channels[index].lower() for x in CHANNEL_EXCLUSIONS):
            continue

        output.append({
            'name': value,
            'channel': channels[index],
            'showtime': showtime.format('DD/MMM/YYYY HH:mm'),
            'timestamp': showtime.timestamp})

    return output


fetch()
