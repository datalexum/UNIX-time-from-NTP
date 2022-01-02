import calendar
import subprocess

from ntplib import NTPClient
from datetime import datetime, timezone, timedelta
from argparse import ArgumentParser
from socket import gaierror


def parse_arguments():
    parser = ArgumentParser(description='Sets the time and date of a unix system from a specified NTP-Server.')

    parser.add_argument('-s',
                        '--server',
                        action='store',
                        type=str,
                        default='pool.ntp.org',
                        help='NTP-Server')
    
    parser.add_argument('-z',
                        '--timezone',
                        action='store',
                        type=int,
                        default=0,
                        help='Hours from UTC')
    
    return vars(parser.parse_args())

def main():
    arguments = parse_arguments()
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


if __name__ == '__main__':
    main()