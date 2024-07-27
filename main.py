# Author: Sam Shenoi
# Description: This file matches mentors and mentees

import argparse
from matching_objects.FileReader import FileReader
from matching_objects.Match import MentorMatch

def main(filename):
    data = FileReader().build(filename)
    man = MentorMatch().match(data["mentors"],data["mentees"])
    print(man)


if __name__ =="__main__":
    parser = argparse.ArgumentParser(
        prog='Simple Mentor Match',
        description='This program matches mentors and mentees based on their specialty preference.',
        epilog='')
    parser.add_argument('filename',help="A file containing both mentors and mentees in a comma seperated value format.")

    args = parser.parse_args()
    main(args.filename)