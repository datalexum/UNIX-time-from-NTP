import calendar
import subprocess

from ntplib import NTPClient
from datetime import datetime, timezone, timedelta
from socket import gaierror


def time_from_ntp(arguments):
    arguments
    ntp_client = NTPClient()
    try:
        response = ntp_client.request(arguments['server'], version = 3)
        response.offset
        time_date = datetime.fromtimestamp(response.tx_time, timezone(timedelta(hours=arguments['timezone'])))

        time_template = "{day} {month} {year} {hour}:{minute}:{second}"
        month = calendar.month_name[time_date.month][:3].upper()

        time_string = time_template.format(day=time_date.day, month=month, year=time_date.year, hour=time_date.hour, minute=time_date.minute, second=time_date.second)
        output = subprocess.check_output(['date', '-s', "{}".format(time_string)])

        print("Time set to {}".format(time_string))
    except gaierror:
        print("Connection Error: No internet connection or connection to NTP-Server not possible!")
    except subprocess.CalledProcessError:
        print("Permission Error: You don't have permissions to set the date and time!")