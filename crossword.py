##################################################################
# FILE : crossword.py
# WRITER : Lior Paz, lioraryepaz, 206240996
# | Eran Gilead, eran.gilead, 203344130
# EXERCISE : intro2cs ex5 2017-2018
# DESCRIPTION : very cool crossword  -you will give us matrix (2d/3d) and
# wanted words - try as big as you want we will never be desperate - and we
# give you how many times your words are there - any direction in the universe.
##################################################################


import math
# for absolute value (fabs)
import initiate as ini

# let us run our central function in a different file

# we chose our code to be modular - we built in separately different funcs,
# and used them all on each other for our final goal

# names for search directions
N = 'u'
S = 'd'
E = 'r'
W = 'l'
NE = 'w'
NW = 'x'
SE = 'y'
SW = 'z'


def create_mat():
    """Opens a matrix text file and turns it into a list of lists - every
    letter is an item in the small lists, every row is an item in the big
    list"""
    mat_file = open(ini.mat_location)
    mat = mat_file.readlines()
    # this is the function that reads a file and turns it into a list
    # according to his rows
    mat_new = []
    # removes "," & "\n" from the items
    for line in mat:
        line = line.lower()
        mat_new.append(list(line.replace(",", "").rstrip()))
    mat_file.close()
    return mat_new


def mat_e(mat):
    """creates all of the possible combinations for east direction"""
    e_words = []
    # the for loops allow us to every time do the following - choose a row,
    # choose starting letter and build all of the options from it
    for row in mat:
        for letter in range(len(row)):
            for i in range(letter, len(row)):
                # creates the words starting at specific 'letter' and loop
                # the options following. we will take the str object for
                # every combination.
                e_words.append(''.join(str(x) for x in (row[letter:i + 1])))
    return e_words


def mat_w(mat):
    """creates all of the possible combinations for west direction"""
    w_words = []
    # the for loops allow us to every time do the following - choose a row,
    # choose starting letter and build all of the options from it
    for row in mat:
        # the -1 is because we run from end to start - the opposite from met_e
        for letter in range(len(row), -1, -1):
            for i in range(letter - 1, -1, -1):
                # only when i counts is 0 then there was a special append so
                #  we wont get out of range
                if i != 0:
                    # w_words.append(row[letter - 1:i - 1:-1])
                    w_words.append(
                        ''.join(str(x) for x in (row[letter - 1:i - 1:-1])))
                else:
                    # w_words.append(row[letter - 1::-1])
                    w_words.append(
                        ''.join(str(x) for x in (row[letter - 1::-1])))
    return w_words


def create_column(mat_new):
    """create a new mat from the original - turns every column to a row by
    order"""
    column_mat = []
    # taking items from the lists by their index number and turns them into
    # a new lst
    for i in range(len(mat_new[0])):
        temp = []
        for j in range(len(mat_new)):
            # first i will be still and j will change - which will give us a
            # column
            temp.append(mat_new[j][i])
        column_mat.append(temp)
    return column_mat


def mat_s(columns):
    """creates all of the possible combinations for south direction"""
    # we implement the east function on the column mat
    s_words = mat_e(columns)
    return s_words


def mat_n(columns):
    """creates all of the possible combinations for north direction"""
    # we implement the west function on the column mat
    n_words = mat_w(columns)
    return n_words


def ne_sw_diagonal(mat_new):
    """create a new mat from the original - turns every
    north-east/south-west diagonal into a list by order"""
    length = len(mat_new)
    length_row = len(mat_new[0])
    ne_sw_mat = []
    counter = 0
    for i in range(length + length_row - 1):
        temp = []
        # the if will help us when the diagonals reach their final
        # phase - while i is out of range, it will stay permanent and
        # counter takes action
        if i > length - 1:
            i = length - 1
            counter += 1
        for j in range(min(i + 1, length_row)):
            # j takes the min range because we want it to grow together with
            #  i but only until the max lenth of the row
            c = j + counter
            # c will be equal to j mostly, it will change only when counter
            # takes action, and help us 'skip' un-wanted items
            if c > length_row - 1:
                # this prevents us from getting out of range
                break
            temp.append(mat_new[i - j][c])
            # every time the row index grows according to j loop
        ne_sw_mat.append(temp)
    return ne_sw_mat


def se_nw_diagonal(mat_new):
    """create a new mat from the original - turns every
    south-east/north-west diagonal into a list by order"""
    length = len(mat_new)
    length_row = len(mat_new[0])
    se_nw_mat = []
    counter = 0
    # now we count from the last index to the first one
    for i in range(length + length_row - 1, 0, -1):
        temp = []
        # we want i to count all of the items up to the first row, but we
        # need to adjust it so we wont get out of range. in addition,
        # once row_i reach 0 we would like to set it as 0 until the end of
        # loop
        row_i = i - length_row
        # if i < length - length_row - 1:
        if i < length_row:
            row_i = 0
            counter += 1
        for j in range(
                min(int(math.fabs(i - (length_row + length))), length_row)):
            # here we used absolute value because i started from it largest
            # val to his smallest, and we will get a negative factor - we
            # need to make it positive.
            # eventually, we want j to run 0-4
            c = j + counter
            # if c > length_row - 1:
            if c > (
                    min(int(math.fabs(i - (length_row + length))),
                        length_row)) - 1:
                break
            temp.append(mat_new[row_i + j][c])
        se_nw_mat.append(temp)
    return se_nw_mat


def mat_ne(ne_sw_mat):
    """creates all of the possible combinations for north-east direction"""
    # we implement the east function on the column mat
    ne_words = mat_e(ne_sw_mat)
    return ne_words


def mat_sw(ne_sw_mat):
    """creates all of the possible combinations for south-west direction"""
    # we implement the west function on the column mat
    sw_words = mat_w(ne_sw_mat)
    return sw_words


def mat_se(se_nw_mat):
    """creates all of the possible combinations for south-east direction"""
    # we implement the east function on the column mat
    se_words = mat_e(se_nw_mat)
    return se_words


def mat_nw(se_nw_mat):
    """creates all of the possible combinations for south-east direction"""
    # we implement the west function on the column mat
    nw_words = mat_w(se_nw_mat)
    return nw_words


def search(mat_new, search_directions):
    """this function is doing the actual building of words combinations"""
    directions = set(search_directions)
    # directions is set to prevent dups
    # the following ifs will run our needed matrix by direction - for every
    # direction of check we need other matrix we have created
    if N in directions or S in directions:
        columns = create_column(mat_new)
    if NE in directions or SW in directions:
        ne_sw_mat = ne_sw_diagonal(mat_new)
    if SE in directions or NW in directions:
        se_nw_mat = se_nw_diagonal(mat_new)
    all_words = []
    for direct in directions:
        # for every direction given we will add his combinations to the
        # overall results lists
        if direct == N:
            all_words.extend(mat_n(columns))
        elif direct == S:
            all_words.extend(mat_s(columns))
        elif direct == E:
            all_words.extend(mat_e(mat_new))
        elif direct == W:
            all_words.extend(mat_w(mat_new))
        elif direct == NE:
            all_words.extend(mat_ne(ne_sw_mat))
        elif direct == SW:
            all_words.extend(mat_sw(ne_sw_mat))
        elif direct == NW:
            all_words.extend(mat_nw(se_nw_mat))
        elif direct == SE:
            all_words.extend(mat_se(se_nw_mat))
    # all_words is the joined combinations for all of the given directions
    return all_words


if __name__ == "__main__":
    # here we start running from cmd and referring to initiate file to start
    #  running the central function.
    ini.initiate()
