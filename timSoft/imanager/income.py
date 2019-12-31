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
    # Options
    # -b, --bare: show unformatted report
    # -c, --category <name> : categorize/tag your expenses
    # -e, --earned: indicates income
    # -f, --file: specifies file name
    # -s [n] : show daily report with total after [n] days
    # -m [n] : show monthly report with total after [n] months
    # -C : Show category/tag-wise report
    # -t, --total: Show just the total when used with -s
    # -M <mm> : Selected the start month (01 <= mm <= 12)
    # -N <mm> : Select an end month (01 <= mm <= 12)
    # -Y <yy> : Select a year (00 <= yy <= 99)
    # -h, --help : Show this help
    # -v, --version: Show version
    pass

def show_info():
    pass


class IncomeManager:
    """Income Manager class."""

    def __init__(self):
        pass

    def main(self):
        pass

    def setup(self):
        # initpem()
        pass
