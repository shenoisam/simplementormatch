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
                    # Create a list of mentors with same speciality interests. First part of list will include those with the same first and
                    #  second order preference as mentee, end of list will include those with switched mentor mentee interests
                    me = matrix[m.order_preferences[i]][m.order_preferences[i+1]] + matrix[m.order_preferences[i+1]][m.order_preferences[i]]
                else:
                    # We don't have enough options so we will have to manually do this,
                    #  or do it randomly
                    me = []
                mentor_missing = self.do_match(m,me)
                # There is a possiblity that there are no matches for this mentee
                #  based on thier first choice. In this case, we will add them to a list
                #  and try again with their second or third choice
                if mentor_missing:
                    temp.append(m)
            missing = temp
            temp = []
            i = i + 1

        # Check to see the ratio of missing mentees
        print(f"{len(missing)/len(mentees)}% mentees unmatched after first pass. Will put remaining mentees with available mentors.")

        # Now for each of the remaining mentees, we have to put them with a proper mentor. We'll have to do this iteratively for now.
        #  This is O(n^2) approach which is very bad... but i have other things to do unfortuntely
        manual_review = []
        for m in missing:
            unmatched = True
            for pref in m.order_preferences:
                mentor_hash = matrix[pref]
                for key in mentor_hash.keys():
                    if unmatched:
                        me = mentor_hash[key]
                        unmatched = self.do_match(m,me)
            if unmatched:
                manual_review.append(m)

        print(f"{len(manual_review)/len(mentees)}% mentees unmatched. Will need to be manually reviewed.")
        self.build_output_files(mentors)
        return manual_review



    def build_output_files(self,mentors):
        f = open("outfile.csv","w")
        f.write("Mentor,Mentee\n")
        for m in mentors:
            for men in m.mentee_list:
                f.write(f"{m.email},{men.email}\n")
        f.close()



    def do_match(self,mentee,mentors):
        mentor_missing = True

        for mz in mentors:
            if len(mz.mentee_list) < self.MAX_MENTEES and mentor_missing:
                mz.mentee_list.append(mentee)
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








