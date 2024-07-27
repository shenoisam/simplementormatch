# Simple Mentor Match
## Overview
This repo contains code for a simple mentor-mentee matching algorithm. The program reads in a list of mentors and mentees from a csv file, matches mentors and mentees together appropriately, and outputs the results to a csv file. It will print the mentees that did not get matched out to the screen

## How To Run
Refer to `sample.csv` file in this repo for an example as to how to set up your excel file for use with this program. Please be sure to have 3 speciality picks for each person for this to work appropriately.

You can run this program with the following command `python3 main.py <filename>` with filename being the path to your excel file

## Outputs
- outfile.csv: This csv file contains the mentor mentee matches
- unmatched people will be printed out to the screen.