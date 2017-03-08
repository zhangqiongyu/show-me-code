#!/usr/bin/env python
#-*-coding=utf-8-*-

import string
import random

SEQ = string.letters + string.digits;

class ActivationCode(object):
    """To generate activation code by the given number"""

    def __init__(self, num, length=15, path = './codes.txt'):
        """Init the class:
            num: the number of the codes
            length: the length of each code
            path: the file path to store the codes"""
        self.num = num;
        self.length = length;
        self.path = path;
        try:
            assert pow(len(SEQ), self.length) > self.num, 'The length of each code is too short, please increase it!'
        except AssertionError, args:
            print '%s: %s' % (args.__class__.__name__, args)
    
    def generate_code(self):
        """Generate the codes using the set list to avoid repeat"""
        codes = {''.join([random.choice(SEQ) for i in xrange(self.length)]) for j in xrange(self.num)}

        with open(self.path, 'w+') as f:
            for item in codes:
                f.write(item + '\n')

if __name__ == '__main__':
    code = ActivationCode(100)
    code.generate_code()
