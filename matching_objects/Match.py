# Author: Sam Shenoi
# Description: This file defines a class that is used for the mentor match program
############ IMPORTS ######################
import copy
from matching_objects.Mentor import Mentor
from matching_objects.Person import Person
############ CODE ######################
class MentorMatch:
    def __init__(self,max_preferences=2, specialty_list=["Cardiology","Heme-Onc","ID","Endocrine","Rheumatology","Pulmonology","Genetics","Allergy","GI","Renal"]):
        self.specialty_list =specialty_list
        self.MAX_PREFERENCES = max_preferences

    #
    # Assumptions
    #   - we want mentor matching to be evenly distributed. To achieve this, we will
    #      cap the number of mentees per mentor at num_mentees/num_mentors
    def match(self,mentors,mentees):
        # Define the maximum number of mentees each mentor can get
        self.MAX_MENTEES = int(len(mentees)/len(mentors)) + 1
        matrix = self.init_array(mentors=mentors)

        missing = mentees
        temp = []
        # Now that the matrix is set up, let's go ahead and match mentees with mentors
        # Ideally, we would use a scoring system to pick the ideal match, but I'm lazy
        #  so this will be a greedy approach
        i = 0
        while i < self.MAX_PREFERENCES:
            for m in missing:
                if len(m.order_preferences) > i +1:
                    mentors = matrix[m.order_preferences[i]][m.order_preferences[i+1]]
                else:
                    # We don't have enough options so we will have to manually do this,
                    #  or do it randomly
                    mentors = []
                mentor_missing = self.do_match(m,mentors)

                # There is a possiblity that there are no matches for this mentee
                #  based on thier first choice. In this case, we will add them to a list
                #  and try again with their second or third choice
                if mentor_missing:
                    temp.append(m)
            missing = temp
            temp = []
            i = i + 1
        [print(m) for m in missing]

    def do_match(self,mentee,mentors):
        mentor_missing = True
        for mz in mentors:
            if len(mz.mentee_list) < self.MAX_MENTEES and mentor_missing:
                mz.mentee_list = mz.mentee_list.append(mentee)
                mentor_missing = False
        return mentor_missing




    #
    # preconditions
    #  - mentors: the list of mentors
    #       - Each mentor will need to have at least 2 speciality preferences for this to work
    # postconditions
    #  - a NxN maxtrix will be constructed with specialities. Mentors will be put in specialities based on this.
    # return: matrix

    def init_array(self,mentors):
        matrix = {}
        for s in self.specialty_list:
            matrix[s] = {}
            for w in self.specialty_list:
                if s != w:
                    matrix[s][w] = []

        for m in mentors:
            matrix[m.order_preferences[0]][m.order_preferences[1]].append(m)

        return matrix








