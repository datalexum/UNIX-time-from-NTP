from utfn.utfn import time_from_ntp
from argparse import ArgumentParser

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
    time_from_ntp(arguments)

if __name__ == '__main__':
    main()