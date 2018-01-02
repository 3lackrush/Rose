#!/usr/bin/env python
#--*-- coding:utf-8 --*--

'''
Author: Kios
Name: Rose
Copyright (c) 2017
'''

from termcolor import colored

def welcome():
    Rose = """
     ____                  ____
    |  _ \ ___  ___  ___  / ___|  ___ __ _ _ __  _ __   ___ _ __
    | |_) / _ \/ __|/ _ \ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
    |  _ < (_) \__ \  __/  ___) | (_| (_| | | | | | | |  __/ |
    |_| \_\___/|___/\___| |____/ \___\__,_|_| |_|_| |_|\___|_|
    """

    Info = """
    -------------------------------------------------------------

    Github: https://github.com/3lackRush
    Twitter: https://twitter.com/LinuxDing
    Telegram: https://t.me/toorKios
    Website: https://www.mkernel.com

    -------------------------------------------------------------
    """
    print(colored(Rose,'red'))
    print(colored(Info,'green'))