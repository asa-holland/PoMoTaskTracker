# Contains the core functions of the Pomo app

import time


def get_formatted_time(raw_seconds):
    # Calculate the time remaining as a sum total of rounded seconds
    time_remaining = int(raw_seconds)

    # calculate hours and update the seconds variable to be without any total hours
    hours = time_remaining // 3600
    time_remaining %= 3600

    # calculate the number of minutes remaining
    minutes = time_remaining // 60
    time_remaining %= 60

    # Calculate total seconds that are not tied up with hours or minutes
    seconds = time_remaining

    result = f'{hours:02}:{minutes:02}:{seconds:02}'
    return result
