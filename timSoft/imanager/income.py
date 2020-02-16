#!/usr/bin/env python3
# This file is part of Tim Software.
from __future__ import print_function, absolute_import, with_statement
import re
import logging
import argparse
import datetime
import time
import os
import os.path

# Global variables
# ver: Version
# prog: Program name
# pemdir: PEM Configuration directory
# fpem: Configuration file
# BARE=0, DAILY=1, MONTHLY=2, CATEGORYWISE=4
# mn = ('Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Sep', 'Oct', 'Nov',
#       'Dec')
# wd = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
#       'Friday', 'Saturady')
#
# ern=0, mode=0, mstep=1, spc='\t', lln=0
# mm=0, em=0, yy=0, tdays=0, totl=0, dfmt="", tag=""


class IncomeError(Exception):
    pass


def parse_option():
    parser = argparse.ArgumentParser()
    # Options
    # -b, --bare: show unformatted report
    parser.add_argument("-v", "--bare", action="store_true",
                        help="show unformatted report")
    # -c, --category <name> : categorize/tag your expenses
    parser.add_argument("-c", "--category", metavar="<name>",
                        help="categorize/tag your expenses")
    # -e, --earned: indicates income
    parser.add_argument("-e", "--earned", help="indicates income")
    # -f, --file: specifies file name
    parser.add_argument("-f", "--file", help="specifies file name")
    # -s [n] : show daily report with total after [n] days
    # USE -d instead of -s as option
    parser.add_argument('-d', '--daily', metavar="[n]", type=int,
                        help="show daily report with total after [n] days")
    # -m [n] : show monthly report with total after [n] months
    parser.add_argument('-m', "--monthly", metavar="[n]", type=int,
                        help="show monthly report with total after [n] months")
    # -C : Show category/tag-wise report
    # TODO: Usage of one-character optional argument
    parser.add_argument("-C", action="store_true",
                        help="Show category/tag-wise report")
    # -t, --total: Show just the total when used with -s
    # TODO: How to to combine to option when used together
    parser.add_argument('-t', '--total', action="store_true",
                        help="show just the total when used with -d")
    # -M <mm> : Selected the start month (01 <= mm <= 12)
    parser.add_argument('-sm', '--start-month', metavar="[N]", type=int,
                        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                        help="select the start month ( 1 <= N <= 12 )")
    # -N <mm> : Select an end month (01 <= mm <= 12)
    parser.add_argument('-em', '--end-month', metavar="[N]", type=int,
                        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                        help="select the end month ( 1 <= N <= 12 )")
    # -Y <yy> : Select a year (00 <= yy <= 99)
    years = list(range(100))
    parser.add_argument('-y', '--year', metavar="[N]", type=int,
                        choices=years,
                        help="select a year ( 1 <= N <= 12 )")
    # -h, --help : Show this help
    # -v, --version: Show version


def show_info():
    pass


class IncomeManager:
    """Income Manager class."""

    def __init__(self):
        self.mode = None #---
        # 
        self.confdir = None # ----

    def main(self):
        pass

    def setup(self):
        # initpem()
        pass
