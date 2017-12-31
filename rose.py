#!/usr/bin/env python
#--*-- coding:utf-8 --*--

'''
Author: Kios
Name: Rose
Copyright (c) 2017
'''

import sys
from lib.core.Spider import SpiderMain
from lib.welcome.welcome import welcome


def main():
    root = "http://wiki.ioin.in/"
    threadNum = 10

    crawler1 = SpiderMain(root, threadNum)
    crawler1.craw()

if __name__ == '__main__':
    welcome()
    main()