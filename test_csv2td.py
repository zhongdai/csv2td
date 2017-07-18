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

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CSV2TDTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
