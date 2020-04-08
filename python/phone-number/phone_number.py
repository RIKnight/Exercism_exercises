#! /usr/bin/env python
"""
    Name:
        phone_number.py
    Purpose:
        exercism, python track, phone_number: 
            Clean up user-entered phone numbers so that they can be sent SMS messages.
    Written by:
        Z Knight, 2020.04.08
"""
class PhoneNumber:
    def __init__(self, number):
        my_number = ""
        for character in number:
            if character in "0123456789":
                # print(character)
                my_number += character

        # check values
        if len(my_number) == 11:
            if my_number[0] == "1":  # trim off the leading 1 to leave 10 digit number
                my_number = my_number[1:]
            else:
                raise ValueError("Phone number with 11 digits must start with 1.")
        if len(my_number) != 10:
            print("not 10 digits")
            raise ValueError("Number does not have 10 digits.")
        elif my_number[0] == "0":
            raise ValueError("Area code can not start with zero.")
        elif my_number[0] == "1":
            raise ValueError("Area code can not start with one.")
        elif my_number[3] == "0":
            raise ValueError("Exchange code can not start with zero.")
        elif my_number[3] == "1":
            raise ValueError("Exchange code can not start with one.")

        self.number = my_number
        self.area_code = my_number[:3]
        self.exchange_code = my_number[3:6]
        self.subscriber = my_number[6:]

    def number(self):
        return self.number

    def pretty(self):
        return f"({self.area_code}) {self.exchange_code}-{self.subscriber}"
