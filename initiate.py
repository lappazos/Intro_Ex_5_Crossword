##################################################################
# FILE : initiate.py
# WRITER : Lior Paz, lioraryepaz, 206240996
# | Eran Gilead, eran.gilead, 203344130
# EXERCISE : intro2cs ex5 2017-2018
# DESCRIPTION : very cool crossword  -you will give us matrix (2d/3d) and
# wanted words - try as big as you want we will never be desperate - and we
# give you how many times your words are there - any direction in the universe.
##################################################################


import sys
# let us  handle cmd
import os
# let us check files
import crossword as cw
# to initiate the search functions
import crossword3d as cwd

NUMBER_OF_ARGUMENTS = 4
# for sys_arg
ERROR_MESSAGE_PARA = 'ERROR: invalid number of parameters. Please enter ' \
                     'word_file' \
                     ' matrix_file output_file directions.'
ERROR_MESSAGE_WORD_LIST = 'ERROR: Word file word_list.txt does not exist'
ERROR_MESSAGE_MATRIX = 'ERROR: Matrix file mat.txt does not exist'
ERROR_MESSAGE_DIR = 'ERROR: invalid directions'

shutdown = False

if len(sys.argv) == NUMBER_OF_ARGUMENTS + 1:
    # the if check for wrong number of arguments
    word_list_location = sys.argv[1]
    mat_location = sys.argv[2]
    output_location = sys.argv[3]
    search_directions = sys.argv[4]
else:
    shutdown = True
    print(ERROR_MESSAGE_PARA)


def create_mat_words():
    """Opens a words text file and turns it into a list"""
    word_list = open(word_list_location)
    # this is the function that reads a file and turns it into a list
    # according to his rows
    mat_words = word_list.readlines()
    mat_words_new = []
    # here we removed from the letters \n
    for word in mat_words:
        word = word.lower()
        # lower the letters if needed
        mat_words_new.append(word.rstrip())
    word_list.close()
    # close the file
    return mat_words_new


def check_mat_empty():
    """checks if mat file is empty and if so - open an empty output file and
     returns empty list for following checks"""
    mat = open(mat_location)
    mat_list = mat.read(1)
    return mat_list


def central():
    """our main function that bring all of the other into action - this is
    the function that runs the course of the search"""
    mat_words_new = create_mat_words()
    if mat_words_new == [] or check_mat_empty() == '':
        # here in case one of the input files is empty - we will return an
        # empty output and finish our run
        output = open(output_location, 'w')
        output.close()
        return
    all_words = []
    # here we divide into 2 course of actions according to the script we ran
    if 'crossword.py' in sys.argv[0]:
        mat_new = cw.create_mat()
        # here we created the mat as a list
        all_words = cw.search(mat_new, search_directions)
        # this is the part where we get allllllll of the possible combinations
        # for words in the mat - not according to the wanted words list
    elif 'crossword3d.py' in sys.argv[0]:
        all_words = cwd.three_d_search(search_directions)
        # this is the part where we get allllllll*n of the possible
        # combinations for words in the matS - not according to the wanted
        # words list
    filtered_all_words = set(all_words)
    # here is rhe same as the last row only without dups - this way we save
    # time counting words that arent found at all
    words_found = dict()
    for word in mat_words_new:
        if word in filtered_all_words:
            # now we are going over all of the words that are actually found
            # and counting them
            words_found[word] = all_words.count(word)
    output = open(output_location, 'w')
    for word in sorted(words_found):
        # here we write our results into file by sorted abc way
        output.write(word + ',' + str(words_found[word]) + '\n')
    output.close()
    # now we will delete the last char \n - not needed
    with open(output_location, 'rb+') as output:
        output.seek(-1, os.SEEK_END)
        output.truncate()


def initiate():
    # here we start running from cmd by all of the different arguments.
    if shutdown:
        # according to if NUMBER OF ARGUMENTS in the top part - shuts down
        # the script if needed
        return
    # the different ifs check for different types of possible errors
    if os.path.isfile(word_list_location):
        if os.path.isfile(mat_location):
            check = True
            for letter in search_directions:
                if 'crossword.py' in sys.argv[0]:
                    if letter not in [cw.N, cw.S, cw.SE, cw.SW, cw.E,
                                      cw.W, cw.NE, cw.NW]:
                        check = False
                        print(ERROR_MESSAGE_DIR)
                        break
                elif 'crossword3d.py' in sys.argv[0]:
                    if letter not in [cwd.WIDTH, cwd.LENGTH, cwd.DEPTH]:
                        check = False
                        print(ERROR_MESSAGE_DIR)
                        break
            if check:
                central()
                # activates the main func if the tests ran successfully
        else:
            print(ERROR_MESSAGE_MATRIX)
    else:
        print(ERROR_MESSAGE_WORD_LIST)
