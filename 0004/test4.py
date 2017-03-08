#!/usr/bin/env python
#-*-coding=utf-8-*-

class ArticleWordNum(object):
    "Get the number of words in an English article"

    def __init__(self, path='./test.txt'):
        self.path = path

    def get_num(self):
        with open(self.path, 'r') as f:
            return len([word for line in f for word in line.split()])

if __name__ == '__main__':
    awn = ArticleWordNum()
    print awn.get_num()
