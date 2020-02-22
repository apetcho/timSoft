#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16, 2020 12:00:13 PM
@author: eapetcho
"""
from datetime import datetime


class RecordInfo:
    """Record information object class"""
    MONTH = (None, "Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    COUNT = 0

    def __init__(self, description, value, tag=None, earning=None):
        self.description = description
        self.value = value
        self.tag = tag
        self.earning = earning
        self.recordId = RecordInfo.COUNT + 1
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        minute = now.minute
        second = now.second
        mn = RecordInfo.MONTH[month]
        self.timestamp = f"{mn}-{day}-{year}T{hour}:{minute}:{second}"

    def set_tag(self, tag):
        """Set A tag for this record."""
        self.tag = tag
        if self.tag is None:
            self.tag = "---"

    def set_earning(self, earning):
        "Set an the earning record."
        self.earning = earning
        if self.earning is not None:
            if is not isinstance(self.earning, (float, int)):
                raise TypeError("The earning value must be a number")

    def get_value(self):
        pass

    def get_description(self):
        pass

    def get_timestamp(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
