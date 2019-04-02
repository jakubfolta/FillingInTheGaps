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
file_regex = re.compile(r'''(spam)     # prefix 'spam'
    (\d+)                              # one or more digits
    (\.txt)                            # file extension
''', re.VERBOSE)

# Set base file number to compare and absolute path to specified directory.
string_filenames = (' '.join(os.listdir(dir_to_check)))

base_filename = file_regex.search(string_filenames)
first_file_number = base_filename.group(2)
abspath = os.path.abspath(dir_to_check)

file = os.listdir(dir_to_check)
range_of_numbers = range(int(first_file_number), int(first_file_number) + len(file))
print(range_of_numbers)
print(first_file_number)

def fix_filename():
    print('Change this directory:\n{}\nto this:\n{}\n'.format(file_abspath, file_new_abspath))
    shutil.move(file_abspath, file_new_abspath)

# Loop through files in specified directory with os.listdir().
num = 1

for file in os.listdir(dir_to_check):

# Search for regex match.
    match = file_regex.search(file)
    if match == None:
        continue
    print(match.group())

# Get regex groups.
    spam = match.group(1)
    number = match.group(2)
    after_number = match.group(3)

# Set new filenames and absolute paths.
    file_abspath = os.path.join(abspath, file)

    digit = 0
    while True:
        changed_filename = spam + str(int(first_file_number) + digit) + after_number
        file_new_abspath = os.path.join(abspath, changed_filename)
        if not os.path.exists(file_new_abspath):
            break
        digit += 1

# Check if filenames are in order.
    if number == first_file_number and number != str(int(first_file_number)):
        print('IF')
        fix_filename()
        continue
    elif number == str(int(first_file_number) + num):
        print('ELIF1')
        num += 1
        continue
    elif number != str(int(first_file_number) + num) and int(number) not in range_of_numbers:
        print('ELIF')
        fix_filename()
        num += 1
        continue
    else:
        print('ELSE')
        continue

# TODO: Change status on github.
'''
