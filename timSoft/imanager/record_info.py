#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16, 2020 12:00:13 PM
@author: eapetcho
"""
from datetime import datetime
from collections import namedtuple


#class Record:
#    """Record Type class"""
#    __slot__=("timestamp","tag", "description","spent","earned","Id")
#
#    def __init__(self, timestamp, tag, description, spent, earned, Id):
#        self.timestamp = timestamp
#        self.tag = tag
#        self.description = description
#        self.spent = spent
#        self.earned = earned
#        self.Id = Id
#
#    @property
#    def timestamp(self):
#        return self.timestamp
#
#    @property
#    def tag(self):
#        return self.tag
#
#    @property
#    def description(self):
#        return self.description
#
#    @property
#    def earned(self):
#        return self.earned
#
#    @property
#    def spent(self):
#        return self.spent
#
#    @property
#    def Id(self):
#        return self.Id
#

class RecordInfo:
    """Record information object class"""
    MONTH = (None, "Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    COUNT = 0
    DEFAULT_TAG = "---"
    #RECORD = namedtuple("RECORD", "timestamp tag description "
    #                    "spent earned Id")
    def __init__(self, description, value, tag=None, earning=None):
        self.description = description
        self.value = value
        self.tag = tag or RecordInfo.DEFAULT_TAG
        self.earning = earning or 0.0
        self.recordId = RecordInfo.COUNT + 1
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        minute = now.minute
        hour = now.hour
        second = now.second
        mn = RecordInfo.MONTH[month]
        self.timestamp = f"{mn}-{day}-{year}T{hour}:{minute}:{second}"

    @staticmethod
    def timestampinfo(recordObj):
        "Return the timestamp detailed information"
        dateinfo, timeinfo = recordObj.timestamp.split('T')
        month, day, year = dateinfo.split("-")
        hour, minute, second = timeinfo.split(":")
        info = {"month": month, "day": day, "year": year,
                "hour": hour, "minute": minute, "second": second}
        return info

    def set_tag(self, tag):
        """Set A tag for this record."""
        self.tag = tag

    def set_earning(self, earning):
        "Set an the earning record."
        self.earning = earning
        if self.earning is not None:
            if not isinstance(self.earning, (float, int)):
                raise TypeError("The earning value must be a number")

    def get_value(self):
        """Returns the expense's value"""
        return self.value

    def get_description(self):
        """Return the description of this record."""
        return self.description

    def get_timestamp(self):
        "Return the timestamp of this record."
        return self.timestamp

    def get_record(self):
        "Return the record"
        #xx = recObj.
        #record = self.timestamp+","+ self.tag+","+self.description
        #record += "," + str(self.value) + "," + str(self.earning)
        #record = str(self.recordId) + "," + record
        #Record = namedtuple("Record",
        #                    ["timestamp", "tag", "description",
        #                     "spent", "earned", "Id"])
        record ={}
        record["ID"] = self.recordId
        record["tag"] = self.tag
        record["spent"] = self.value
        record["earned"] = self.earning
        record["timestamp"] = self.timestamp
        record["description"] = self.description
        return record

    def __str__(self):
        record = self.get_record_line()
        return f"{record}"

    def __repr__(self):
        desc = self.description
        val = self.value
        tag = self.tag
        earning = self.earning
        return "RecordInfo({!r}, {!r}, tag={!r},earning={!r})".format(
                desc, val, tag, earning)
