import csv
import re

f = open('output.csv','w') # output file

csv_file = csv.reader(open("input.csv", "r"), delimiter="_") # read in csv and declare delimitter

regex_txt = r"^[a-zA-Z]{3}[0-9]{5}$" # what you're looking for

listLines = [] # Dupe catcher

pattern = re.compile(regex_txt, re.IGNORECASE) # pattern which ignores case so TUGxxxxx is permissable

for row in csv_file: # grab row
    for s in row: # grab chunk
        if s in listLines: # skip if already in use
            continue 
        
        else: # add the good stuff 
            if pattern.search(s):
                f.write(s+"\n")
                listLines.append(s)





