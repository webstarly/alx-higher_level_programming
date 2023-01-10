#!/usr/bin/python3

"""

Contains class MyList

inherits from list; has public instance method to print sorted

"""


MyList = __import__('1-my_list').MyList


class MyList(list):

    """inherits from list

    methods:

    print_sorted(self)

    """

    def print_sorted(self):

        """prints list of ints all sorted in ascending order"""

        print(sorted(self))
