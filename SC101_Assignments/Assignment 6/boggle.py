"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


# dict_lst = []


def main():
    """
	TODO:
	"""
    start = time.time()
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################

    count = 1
    matrix = []
    while count < 5:
        row = input(f'{count} row of letters: ')
        row = row.lower()
        if check_format(row):
            row = row.split()
            matrix.append(row)
            count += 1
        else:
            print("Illegal input")
    print(matrix)

    # test case
    # matrix = [['f', 'y', 'c', 'l'],  # 0
    #           ['i', 'o', 'm', 'g'],  # 1
    #           ['o', 'r', 'i', 'l'],  # 2
    #           ['h', 'j', 'h', 'u']]  # 3
    dict_lst = read_dictionary(matrix)
    result = boggle(matrix, dict_lst)
    print(f'the words are: {result}')
    print(f'{len(result)} words found')

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(board, dict_lst):
    final_lst = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            print(f'current focus: {board[x][y]}')
            coordinates = [(x, y)]
            cur_s = board[x][y]
            final_lst = boggle_helper(dict_lst, board, x, y, coordinates, cur_s, final_lst)
    return final_lst


def boggle_helper(dict_lst, board, x, y, coordinates, cur_s, cur_lst):
    if len(cur_s) >= 4:
        if cur_s not in cur_lst and cur_s in dict_lst:
            cur_lst.append(cur_s)
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i <= 3 and 0 <= j <= 3:  # edges of the board are (0,0/0,3/3,0/3,3)
                if (i, j) not in coordinates:
                    ch = board[i][j]
                    coord = (i, j)
                    # Choose
                    coordinates.append(coord)
                    cur_s += ch
                    # Explore
                    if has_prefix(cur_s, dict_lst):
                        boggle_helper(dict_lst, board, i, j, coordinates, cur_s, cur_lst)
                    # Un-choose
                    cur_s = cur_s[:-1]
                    coordinates.pop()
    return cur_lst


def check_format(letters):
    if len(letters) != 7:
        return False
    for i in range(len(letters)):
        ch = letters[i]
        if i % 2 == 1 and ch != ' ':
            return False
        if i % 2 == 0 and not ch.isalpha():
            return False
    return True


def read_dictionary(s):
    """
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
    dict_lst = []
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) >= 4:
                for i in range(len(s)):
                    for j in range(len(s[i])):
                        ch = s[i][j]
                        if word.startswith(ch):
                            dict_lst.append(word)
    return dict_lst


def has_prefix(sub_s, dict_lst):
    """
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
    for word in dict_lst:
        # word = dict_lst[i]
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
