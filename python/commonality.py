#! /usr/bin/env python
"""
    Name:
        commonality.py
    Purpose:
        write a function that takes two iterables,
        returns common itiems
    Modification History:
        Written by Z Knight, 2020.06.24
"""
def find_common(input_1, input_2):
    # print(input_1, input_2)

    result = []
    for item1 in input_1:
        for item2 in input_2:
            if item1 == item2:
                result.append(item1)

    return(result)

###
# test it

if __name__=="__main__":
    t1 = ['a','b','c']   
    t2 = ['a','c','d']  


    result = find_common(t1, t2)
    print(result)

