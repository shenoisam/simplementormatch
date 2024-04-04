# Author: Sam Shenoi
# Description: This file defines a class that is used for the mentor match program
import copy
import csv

class Person:
    def __init__(self,email):
        self.email = email
        self.order_preferences = []
class Mentor(Person):
    def __init__(self, email):
        super().__init__(email)
        self.mentee_list = []
class FileReader:
    def __init__(self):
        self.MENTOR_NDX = 1
        self.EMAIL_NDX = 0
        self.PREFERENCES = 2
    def build(self,filename):
        data = []
        with open(filename, newline='\n') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                if row[self.MENTOR_NDX] == self.MENTOR_NDX:
                    data.append(Mentor(email=row[self.EMAIL_NDX],order_preferences=row[self.PREFERENCES:]))
                else:
                    data.append(Person(email=row[self.EMAIL_NDX],order_preferences=row[self.PREFERENCES:]))
        return data



class MentorMatch:
    def __init__(self, num_preferences = 3):
        self.num_mentees = 1
        self.num_preferences = num_preferences
    def match(self,mentor_list, mentee_list):
        self.num_mentees = len(mentee_list)
        for m in mentee_list:
            best_score = 10000
            best_mentor = None
            for e in mentor_list:
                score = self.__calculate_score(m,e)
                if score < best_score:
                    best_score = score
                    # Create a shallow copy (aka pointer) for the best mentor
                    best_mentor = copy.copy(e)
            best_mentor.mentee_list.append(m)

    def __calculate_score(self,mentee,mentor):
        score = len(list(set(mentee.order_preferences + mentor.order_preferences)))/self.num_preferences
        score = score + len(mentor.mentee_list)
        return score


