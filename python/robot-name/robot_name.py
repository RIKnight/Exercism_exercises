#! /usr/bin/env python
"""
    Name:
        robot_name.py
    Purpose:
        exercism, python track, robot_name
    Written by:
        Z Knight, 2019.10.09
"""
import string
import random

class Robot(object):
    # class level list to store all robot names
    name_store = []

    def __init__(self):
        self.reset()

    def _randUPPER(self):
        return random.choice(string.ascii_uppercase)

    def _randint(self):
        return str(random.randint(0,9))

    def reset(self):
        unique_name = False
        while not unique_name:
            name = ""
            name += self._randUPPER()
            name += self._randUPPER()
            name += self._randint()
            name += self._randint()
            name += self._randint()
                    
            # is this name taken?
            if name not in Robot.name_store:
                Robot.name_store.append(name)
                unique_name = True
        self.name = name

