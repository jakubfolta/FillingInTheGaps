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

# Set base file number to compare.
string_filenames = (' '.join(os.listdir(dir_to_check)))
base_filename = file_regex.search(string_filenames)
first_file_number = base_filename.group(2)

def fix_filename():
    print('Change this directory: {}\nto this:\n{}'.format(file_abspath, file_new_abspath))
    #shutil.move(file_abspath, file_new_abspath)
def fix_filename_number():
    print('Change this directory: {}\nto this:\n{}'.format(file_abspath, file_new_number_abspath))
    #shutil.move(file_abspath, file_new_number_abspath)

# Loop through files in specified directory with os.listdir().
num = 1

for file in os.listdir(dir_to_check):
    abspath = os.path.abspath(dir_to_check)
    file_abspath = os.path.join(abspath, file)

# Search for regex match.
    match = file_regex.search(file)
    if match == None:
       continue

# Get regex groups.
    spam = match.group(1)
    number = match.group(2)
    after_number = match.group(3)

    changed_filename = spam + str((int(number))) + after_number
    changed_filename_number = spam + str((int(first_file_number) + num)) + after_number

    file_new_abspath = os.path.join(abspath, changed_filename)
    file_new_number_abspath = os.path.join(abspath, changed_filename_number)

# Check if filenames are in order.
    if number == first_file_number:
        fix_filename()
        continue
'''
    elif int(number) == int(first_file_number) + num:

        num += 1
        continue
    else:
        print(next_in_order_filename)

# Set abs path for new filename.
        old_filename_abspath = os.path.join(abspath, file)
        new_filename_abspath = os.path.join(abspath, next_in_order_filename)
        print(abspath)
        print(old_filename_abspath)
        print(new_filename_abspath)
        num += 1


# Change filename.
        print('Change this filename: {}\nto this:\n{}'.format(old_filename_abspath, new_filename_abspath))
        #shutil.move(old_filename_abspath, new_filename_abspath)

# TODO: Change status on github.
'''
