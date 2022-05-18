"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dict_lst = []                      # dictionary lst

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
    while True:
        s = input("Find anagram for: ")
        if s == EXIT:
            break
        else:
            read_dictionary(s)
            x = find_anagrams(s)
            print(f'{len(x)} anagrams: {x}')

    # s = 'arm'  # test case 1
    # s = 'contains'  # test case 2
    # s = 'stop'  # test case 3

    # read_dictionary(s)
    # print(read_dictionary(s))
    # print(len(dict_lst))

    # x = find_anagrams(s)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')
    # find_anagrams(s)


def read_dictionary(s):
    for i in range(len(s)):
        ch = s[i]
        # print(ch)
        with open(FILE, 'r') as f:
            for line in f:
                word = line.strip()
                if word.startswith(ch) and len(word) == len(s):
                    dict_lst.append(word)
                    # print(word)
    return dict_lst


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    new_lst = []
    word_var = find_anagrams_helper(s, len(s), [], [], [])  # three lists are curr_lst, new_lst, index_lst, respectively
    # print(f'word_var = {word_var}')
    # print(type(word_var))
    for i in range(len(word_var)):
        var = word_var[i]
        if var in dict_lst:
            print("Search...")
            new_lst.append(var)
            print(f"Found: {var}")
    return new_lst


def find_anagrams_helper(s, len_s, curr_lst, index_lst, result_lst):
    if len(curr_lst) == len_s:  # join words when word length reached
        word = ''.join(curr_lst)
        if word not in result_lst:  # precludes repeated words, i.e., "stops" vs "stops" (the "s"'s are technically different)
            result_lst.append(word)
    else:
        for i in range(len_s):
            ch = s[i]  # split into characters
            # print(ch)
            if i not in index_lst:
                index_lst.append(i)
                # Choose
                curr_lst.append(ch)
                # Explore
                # for j in range(len(dict_lst)):
                #     dict_word = dict_lst[j]
                if has_prefix(s):
                    find_anagrams_helper(s, len_s, curr_lst, index_lst, result_lst)  # fix s
                # Un-choose
                curr_lst.pop()
                index_lst.pop()
    return result_lst


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for i in range(len(dict_lst)):
        word = dict_lst[i]
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
