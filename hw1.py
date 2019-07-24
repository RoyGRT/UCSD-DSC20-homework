"""
HW1 DSC20 Spring 2019
Name of Student:Ruotian Gao
PID of Student:A15230548
"""

def missing_number(lst):
    """ Given a list that contains distinct integers 0 through n 
    in any order, return the number that is missing from the list

    >>> lst = [1, 0, 3, 4]
    >>> missing_number(lst)
    2
    >>> lst = [0, 1, 4, 2]
    >>> missing_number(lst)
    3
    >>> lst = [2, 1, 5, 4, 3]
    >>> missing_number(lst)
    0
    """
    
    # YOUR CODE IS HERE #
    return (set(range(len(lst)))-set(lst)).pop()

def prime_list_reversed(x, y):
    """
    Input: the number x and y
    Output: all prime numbers within [x,y] in reverse order

    >>> prime_list_reversed(3, 10)
    [7, 5, 3]
    >>> prime_list_reversed(3, 3)
    [3]
    >>> prime_list_reversed(1, 15)
    [13, 11, 7, 5, 3, 2, 1]
    """
    assert type(x) is int, "first argument must be an integer"
    assert type(y) is int, "second argument must be an integer"
    assert x > 0, "first argument must be positive"
    assert y >= x, "second argument must be >= the first one"
    value = []
    nums = list(range(x,y+1))
    for i in nums:
        di = 0
        for j in range(1,i+1):
            if i % j == 0:
                di += 1
        if di == 2 or i == 1:
            value.append(i)
    return value[::-1]

def clever_average(nums):
    """
    >>> clever_average([4, 0, 100])
    4
    >>> clever_average([7, 7, 7])
    7
    >>> clever_average([-10, -4, -2, -4, -2, 0])
    -3
    """

    assert type(nums) is list,"Input must be a list"

    return (sum(nums)-min(nums)-max(nums))//(len(nums)-2)

def in_or_out(outer_list, inner_list):
    """
    >>> in_or_out([-1, 0, 3, 3, 3, 10, 12], [-1, 0, 3, 12])
    True

    >>> in_or_out([3, 4, 7, 8], [2, 3, 4]) 
    False

    >>> in_or_out([2, 2, 4, 4, 6], [2, 4])
    True
    """

    assert type(outer_list) is list and type(inner_list) is list,"Both inputs must be lists"

    for i in inner_list:
        if i not in outer_list:
            return False
    return True

def numbered_rows (levels = 10):
    """
    >>> numbered_rows()
    1 * 1 2 3 4 5 6 7 8 9 10
    2 * 2 4 6 8 10 12 14 16 18 20
    3 * 3 6 9 12 15 18 21 24 27 30
    4 * 4 8 12 16 20 24 28 32 36 40
    5 * 5 10 15 20 25 30 35 40 45 50
    6 * 6 12 18 24 30 36 42 48 54 60
    7 * 7 14 21 28 35 42 49 56 63 70
    8 * 8 16 24 32 40 48 56 64 72 80
    9 * 9 18 27 36 45 54 63 72 81 90
    10 * 10 20 30 40 50 60 70 80 90 100
    >>> numbered_rows(4)
    1 * 1 2 3 4
    2 * 2 4 6 8
    3 * 3 6 9 12
    4 * 4 8 12 16
    """
    nums = list(range(1,levels+1))
    for i in nums:
        newlist = [j*i for j in nums]
        to_print = ''
        for j in newlist:
            to_print += str(j)
            if j!=i * levels:
                to_print += ' ' 
        print(str(i),'*',to_print)
