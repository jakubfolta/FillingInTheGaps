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
spam_regex = re.compile(r'''(spam)      # "spam" word in filename
                            (\d+)       # one or more digits
                            (\.txt)     # ".txt" at the end of filename
''', re.VERBOSE)

# Get first matched file and number of first file.
first_matched_file = spam_regex.search(' '.join(os.listdir(dir_to_check)))
first_file_number = first_matched_file.group(2)

# Get number of matched files and set range of numbers for files in given directory.
number_of_matches = len(spam_regex.findall(' '.join(os.listdir(dir_to_check))))
range_for_filenumbers = range(int(first_file_number), int(first_file_number) + number_of_matches)
list_of_filenumbers = list(range_for_filenumbers)
print('Range for filenumbers:\n{}\n'.format(list_of_filenumbers))

# Create funtion to change filenames.
def fix_filename():
    print('Change this filename: {}\nto this:\n{}'.format(file, new_filename))
    shutil.move(file_abspath, newfile_abspath)
    print('Filename fixed!\n')

# Use for loop and os.listdir() to check files.
for file in os.listdir(dir_to_check):
    match = spam_regex.search(file)
    if match == None:
        continue

# Set absolute path to old file.
    file_abspath = os.path.join(dir_to_check, file)

# Get matched file groups.
    spam = match.group(1)
    number = match.group(2)
    file_ext = match.group(3)

# Create new filename with while loop.
    num = 0
    while True:
        new_filename = spam + str(int(first_file_number) + num) + file_ext
        newfile_abspath = os.path.join(dir_to_check, new_filename)
        if not os.path.exists(newfile_abspath):
            break
        num += 1

# Check files.
    if number == str(int(number)) and int(number) in range_for_filenumbers:
        print('File "{}" in range for filenumbers.\n'.format(match.group()))
        continue
    else:
        fix_filename()
else:
    print('All filenames in order!')
