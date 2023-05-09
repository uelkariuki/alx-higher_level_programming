#!/usr/bin/python3
def lowercaseAlph():

    for a in range(97, 123):
        if a != 113 and a != 101: 
            print('{:c}'.format(a), end='')


lowercaseAlph()
