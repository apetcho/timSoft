#!/usr/bin/env python3
# This file is part of Tim Software.
#
from __future__ import (print_function, with_statement, division,
                        absloute_import)
import os
import re
import time
import datetime
import logging

#my ($ver, $prog, $pemdir, $fpem) = ("0.7.9", "", "", "");
#my ($BARE, $DAILY, $MONTHLY, $CATEGORYWISE) = (0, 1, 2, 4);

#my @mn = qw( Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec );
#my @wd = qw( Sunday Monday Tuesday Wednesday Thursday Friday Saturday );

#my ($ern, $mode, $mstep, $spc, $lln) = (0, 0, 1, "\t", 0);
#my ($mm, $em, $yy, $tdays, $totl, $dfmt, $tag) = (0, 0, 0, 0, 0, "", "");


class Operations:

    def __init__(self):
        # 1- set the current year
        # 2- check the existence of USERPROFILE environment variable: if
        # no, raise an exception and quit.
        # if yes, get it set its value to a local variable
        # 3- mode: variable that tell whether to create 
        pass

    def _daily(self):
        pass

    def _daily_bare(self):
        pass

    def _monthly(self):
        pass

    def _categorywise(self, file=None):
        """Shows cumulative income/expenses for each tag or category.

        Parameters
        ----------

        file: str
            record file to be analyzed."""
        pass

    def _line(self, c='-', nc=65):
        """Prints a line consisting of a character pattern.

        Parameters
        ----------
        c: char
            Character pattern used to draw the line [default: '-'']

        nc: int
            Number of character pattern constituting the line drawn.
            [default: 65]
        """
        line = c*nc + '\n'
        print(line)

    def _is_subset(self, arg1, arg2):
        """Checks if arg2 is a subset of arg1.

        Parameters
        ----------
        arg1, arg2: set
            Set of items

        Returns
        -------
        True if arg2 is subset of arg1 otherwise False."""
        pass

    def _ndays(self, datetimeObj):
        """Return the number of days in the corresponding month
        of a datetime object.

        Parameters
        ----------
        datetimeObj: datetime object
            Datetime object for which the number of the corresponding
            month is request.

        Returns
        -------
        n: int
            Total number of days in a month.
        """
        pass

    def _show_total(self, *args):
        pass

    def _show(self, *args):
        pass
