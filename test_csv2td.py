#!/usr/bin/env python

"""Tests for Wbteq"""
import os
import unittest

from csv2td import csv2td


class CSV2TDTestCase(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        pass

    def tearDown(self):
        pass

    def test_import(self):
        self.assertTrue(True)

    def test_long_object_name(self):
        object_name = "aaaaabbbbccccddddddfaaaaaajjjjjjkkkkkkllllllddddddd"
        self.assertEqual(object_name[:30],
                         csv2td.correct_object_name(object_name))

    def test_name_has_space(self):
        object_name = "abc ddd efg"
        self.assertEqual(object_name.replace(" ","_"),
                         csv2td.correct_object_name(object_name))

    def test_name_has_speical_chars(self):
        object_name = "abc$ddd%efg"
        self.assertEqual("abc_ddd_efg",
                         csv2td.correct_object_name(object_name))

    def test_name_starts_with_number(self):
        object_name = "123iloveyou"
        self.assertEqual("_123iloveyou",
                         csv2td.correct_object_name(object_name))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CSV2TDTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
