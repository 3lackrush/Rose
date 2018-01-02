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
import argparse


def main():
    parser = argparse.ArgumentParser(description='Rose Scanner Help.')
    parser.add_argument("-t", "--target", type=str, help="Add root url of the target site!")
    parser.add_argument("-n", '--number', type=int, help="Add thread number!")
    args = parser.parse_args()
    root = args.target
    threadNum = args.number

    crawler1 = SpiderMain(root, threadNum)
    crawler1.craw()

if __name__ == '__main__':
    welcome()
    main()
