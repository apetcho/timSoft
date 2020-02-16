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
    def __init__(self, description, value, tag=None, earning=None):
        self.description = description
        self.value = value
        self.tag = tag
        self.earning = earning
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        minute = now.minute
        second = now.second
        mn = RecordInfo.MONTH[month]
        self.timestamp = f"{mn}-{day}-{year}T{hour}:{minute}:{second}"

    def set_tag(self, tag):
        pass

    def set_earning(self, earning):
        pass

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
