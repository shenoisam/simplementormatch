# Author: Sam Shenoi
# Description: This file matches mentors and mentees

import argparse

def main():
    print("Temp")

if __name__ =="__main__":
    parser = argparse.ArgumentParser(
        prog='Simple Mentor Match',
        description='This program matches mentors and mentees based on their specialty preference.',
        epilog='')
    parser.add_argument('filename')

    args = parser.parse_args()
    main()