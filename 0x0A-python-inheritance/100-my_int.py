#!/usr/bin/python3
"""
contains class MyInt
"""


class MyInt(int):
    """ defines class MyInt """
    def __new__(clas, *args, **kwargs):
        """ create new instance of class """
        return super(MyInt, clas).__new__(clas, *args, **kwargs)

    def __eq__(self, other):
        """ != is now == """
        return int(self) != other

    def __ne__(self, other):
        """ == is now != """
        return int(self) == other
