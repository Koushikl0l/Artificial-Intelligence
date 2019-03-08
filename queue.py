#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 08:45:44 2018

@author: koushikahamed
"""

class Queue:
    """Simple FIFO queue"""
    def __init__(self, element=None):
        self.data = []

    def empty(self):
        return True if len(self.data)==0 else False

    def append(self, element):
        self.data.append(element)

    def insert_all(self, element):
        for i in element:
            self.data.append(i)

    def first(self):
        return self.data[0]

    def pop(self):
        return self.data.pop(0)

    
