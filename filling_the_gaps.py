#! python3

'''filling_the_gaps.py - A program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on,
in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Program rename all the later files to close this gap.
'''

# Import essential modules.
import re
import os
import shutil

# Set directory to check.
dir_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects\FillingInTheGaps\check'

# Write regex to find files with given prefix.
file_regex = re.compile(r'''(^spam)   # filename begin with 'spam'
    (\d+)                               # one or more digits
    (.*)$                               # all text after digits
''', re.VERBOSE)

# Loop through files in specified directory with os.listdir().
for file in os.listdir(dir_to_check):
    print(file)
# Search for regex match.
    match = file_regex.search(file)
    if match == None:
        continue
    print(match.group())

# Get regex groups.
    spam = match.group(1)
    number = match.group(2)
    after_number = match.group(3)

# TODO: Fill in the gaps in the filenames.
# TODO: Change status on github.
