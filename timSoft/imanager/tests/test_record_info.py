#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22, 2020 11:26:22 AM
@author: eapetcho
"""
import unittest
from timSoft.imanager.record_info import RecordInfo

# Input data for testing purpose
description = "Bus ticket"
value = 60.12
recObj = RecordInfo(description, value)
now = recObj.timestamp


class TestRecordInfo(unittest.TestCase):

    def test_timestampinfo(self):
        """Test timestampinfo() method"""
        dateinfo, timeinfo = now.split('T')
        month, day, year = dateinfo.split('-')
        hour, minute, second = timeinfo.split(':')
        info = {'month': month, "day": day, "year": year,
                "hour": hour, "minute": minute, "second": second}
        print("Testing timestampinfo() method")
        self.assertEqual(RecordInfo.timestampinfo(recObj), info)
        print("Test finished")

    def test_set_tag(self):
        pass

    def test_set_earning(self):
        pass

    def test_get_value(self):
        pass

    def test_get_description(self):
        pass

    def test_get_timestamp(self):
        pass

    def test_get_record_line(self):
        pass


if __name__ == "__main__":
    unittest.main()
