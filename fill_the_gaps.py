#!python3

'''fill_the_gaps.py - A program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on,
in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Program rename all the later files to close this gap.'''

# Import essential modules.
import os
import re
import shutil

# Set directory to check.
dir_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects\FillingInTheGaps\check'

# Create regex.
spam_regex = re.compile(r''' ^(spam)    # "spam" word in filename
    (\d+)                               # one or more digits
    (\.txt)                             # ".txt" at the end of filename
''', re.VERBOSE)

# Use for loop and os.listdir() to check files.
for file in os.listdir(dir_to_check):
    match = spam_regex.search(file)
    if match == None:
        continue
    print(match.group())

# Get matched file groups.
    spam = match.group(1)
    number = match.group(2)
    file_ext = match.group(3)


# TODO: Create new filename with while loop.


# TODO: Search regex.
# TODO:
# TODO:
