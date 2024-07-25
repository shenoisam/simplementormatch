# Author: Sam Shenoi
# Description: This file contains a class to read in data from a csv file.

############ IMPORTS ######################
import csv
from matching_objects.Mentor import Mentor
from matching_objects.Person import Person

############ CODE ######################
class FileReader:
    def __init__(self):
        self.MENTOR_NDX = 1
        self.EMAIL_NDX = 0
        self.PREFERENCES = 2

    # input:
    #  - self: default parameter for self object
    #  - filename: the name of the csv file contaning the mentees and mentors
    #          csv file should have the following parmeters as provided in sample csv file
    # output: a combined list of mentors and person objects
    def build(self,filename):
        data = {"mentors":[],"mentees":[]}
        with open(filename, newline='\n') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            first_row = True
            for row in spamreader:
                if not first_row:
                    # If the read in line is a mentor (ie the isMentor field is set to 1), we will treat them as such
                    if bool(int(row[self.MENTOR_NDX])):
                        data["mentors"].append(Mentor(email=row[self.EMAIL_NDX],preferences=list(row[self.PREFERENCES:])))
                    else:
                        data["mentees"].append(Person(email=row[self.EMAIL_NDX],preferences=list(row[self.PREFERENCES:])))
                first_row = False
        return data
