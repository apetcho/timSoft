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
        print("\nTesting timestampinfo() method")
        self.assertEqual(RecordInfo.timestampinfo(recObj), info)
        print("Testing timestampinfo() method finished.")

    def test_set_tag(self):
        """Test set_tag method"""
        print("\nTesting set_tag() method")
        tag = "transport"
        recObj.set_tag(tag)
        self.assertEqual(recObj.tag, tag)
        print("Testing set_tag() method finished.")

    def test_set_earning(self):
        """Test set_earning method"""
        earning = 1800.0
        recObj.set_earning(earning)
        print("\nTesting set_earning() method")
        self.assertEqual(recObj.earning, earning)
        print("Testing set_earning() method finished.")

    def test_get_value(self):
        """Test get_value method"""
        print("\nTesting get_value() method")
        self.assertEqual(recObj.get_value(), value)
        print("Testing get_value() method finished.")

    def test_get_description(self):
        """Test get_description method"""
        print("\nTesting get_description() method")
        self.assertEqual(recObj.get_description(), description)
        print("Testing get_description() method finished.")

    def test_get_timestamp(self):
        """Test get_timestamp() method"""
        print("\nTesting get_timestamp() method")
        self.assertEqual(recObj.get_timestamp(), recObj.timestamp)
        print("Testing get_timestamp() method finished.")

    def test_get_record_line(self):
        pass


if __name__ == "__main__":
    unittest.main()
