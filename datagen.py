# Author: Sam Shenoi
# Description: This file generates test cases for mentee matching problem
import random

SPEC_LIST =["Cardiology","Heme-Onc","ID","Endocrine","Rheumatology","Pulmonology","Genetics","Allergy","GI","Renal"]
NUM_PREF = 3
def main(total=100,mentor_ratio=.2):
    mentor_count = int(total * mentor_ratio)
    mentee_count = total - mentor_count

    f = open("./testdata.csv",'w')
    f.write("email,isMentor,preferences\n")
    for i in range(0,mentor_count):
        f.write(f"Mentor{i},1,{','.join(random.sample(SPEC_LIST,NUM_PREF))}\n")
    for i in range(0,mentee_count):
        f.write(f"Mentee{i},0,{','.join(random.sample(SPEC_LIST,NUM_PREF))}\n")

    f.close()


if __name__ =="__main__":
    main()
