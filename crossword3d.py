##################################################################
# FILE : crossword3d.py
# WRITER : Lior Paz, lioraryepaz, 206240996
# | Eran Gilead, eran.gilead, 203344130
# EXERCISE : intro2cs ex5 2017-2018
# DESCRIPTION : very cool crossword  -you will give us matrix (2d/3d) and
# wanted words - try as big as you want we will never be desperate - and we
# give you how many times your words are there - any direction in the universe.
##################################################################

import crossword as cw
# in order to use main search func
import initiate as ini
# let us run our central function in a different file

# names for search directions
DEPTH = 'a'
LENGTH = 'b'
WIDTH = 'c'


def split_mats():
    """split our 3d matrix into a list of separated 2d mats"""
    three_d_mat = open(ini.mat_location)
    # here we open the file
    three_d_list = three_d_mat.readlines()
    # converting the file into lists
    mats_list_depth = []
    last_index = 0
    # needed for the separation process - remember where have we stopped
    for (index, line) in enumerate(three_d_list):
        # this loop runs on the marix list and gives us exac location for
        # every line by index
        three_d_list[index] = list(line.replace(",", "").rstrip())
        # here we are stripping the data from unwanted chars
        if line == '***\n':
            mats_list_depth.append(three_d_list[last_index:index])
            last_index = index + 1
    mats_list_depth.append(three_d_list[last_index:])
    return mats_list_depth


def convert_to_length(mats_list_depth):
    """takes the basic 2d mats list and convert them into length mats - every
    i line from every mat becomes part of mat i in the new set"""
    mats_list_length = []
    for i in range(len(mats_list_depth[0])):
        # this loop gives us the range of new mats we will get
        temp = []
        for j in range(len(mats_list_depth)):
            # this gives us the number of lines in every new mat we create
            temp.append(mats_list_depth[j][i])
        mats_list_length.append(temp)
    return mats_list_length


def convert_to_width(mats_list_depth):
    """takes the basic 2d mats list and convert them into width mats - every i
     column from every mat becomes part of mat i in the new set"""
    mats_list_width = []
    for i in range(len(mats_list_depth[0][0])):
        # this loop gives us the range of new mats we will get
        temp = []
        for j in range(len(mats_list_depth)):
            # this gives us the number of lines in every new mat we create
            temp_temp = []
            for k in range(len(mats_list_depth[0])):
                # this gives us the number of items in every line in the new
                #  mats
                temp_temp.append(mats_list_depth[j][k][i])
            temp.append(temp_temp)
        mats_list_width.append(temp)
    return mats_list_width


def three_d_search(search_directions):
    """this function will refrence every a,b,c direction to the cw.search
    func, and in total will give us the included amount of possible words
    through-out the entire 3d construction"""
    mats_list_depth = split_mats()
    # here we created the mats as a list
    directions = set(search_directions)
    # directions is set to prevent dups
    all_words = []
    for direct in directions:
        # for every direction given we will add his combinations to the
        # overall results lists - according to the parallel cw.search
        if direct == DEPTH:
            for mat in mats_list_depth:
                all_words.extend(cw.search(mat, 'udrlwxyz'))
        elif direct == LENGTH:
            mats_list_length = convert_to_length(mats_list_depth)
            for mat in mats_list_length:
                all_words.extend(cw.search(mat, 'udrlwxyz'))
        elif direct == WIDTH:
            mats_list_width = convert_to_width(mats_list_depth)
            for mat in mats_list_width:
                all_words.extend(cw.search(mat, 'udrlwxyz'))
    # all_words is the joined combinations for all of the given directions
    return all_words


if __name__ == "__main__":
    # here we start running from cmd and referring to initiate file to start
    #  running the central function.
    ini.initiate()
