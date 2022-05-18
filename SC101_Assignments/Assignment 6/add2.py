"""
File: add2.py
Name:
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    #                     #
    #        TODO:        #
    #                     #
    #######################
    if l1.val == 0 and l2.val == 0:
        return l1
    c_l1 = l1
    c_l2 = l2
    str_cl1 = make_string(c_l1)  # ListNode is converted to string form
    str_cl2 = make_string(c_l2)
    rev_1 = reverse_string(str_cl1)  # ListNode string is reversed
    rev_2 = reverse_string(str_cl2)
    rev_result = int(rev_1) + int(rev_2)  # Int form of ListNode is added
    result = make_listnode(str(rev_result))  # Str form of str_rev_result is converted to ListNode form
    return result
    # can reverse into string make int (precludes 0's), then reverse back into string
    # i.e., 1900 -> "1900" -> "0091" -> 91 -> list node form = 1 -> 9


def make_listnode(string):
    node_old = None  # can also just init first node with node_old = (int(string[0]), None)
    linked_list = node_old
    for i in range(len(string)):
        ch = string[i]
        if i == 0:  # first node, which is the final node in the linked_list
            node_old = ListNode(int(ch), None)
        else:
            node_new = ListNode(int(ch), node_old)  # links node_new to node_old, reversing the string naturally
            node_old = node_new  # saves node_new as node_old
            linked_list = node_old
    return linked_list


def reverse_string(string):  # takes in string, returns reversed string
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string


def make_string(list_node):  # takes in ListNode, converts, returns string form of ListNode
    cur = list_node
    new = ''
    while cur is not None:
        # print(f'cur: {cur.val}')
        new += str(cur.val)
        cur = cur.next
    return new


####### DO NOT EDIT CODE BELOW THIS LINE ########

def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
