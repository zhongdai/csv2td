#!/usr/bin/env python

"""Tests for Wbteq"""
import os
import unittest
from io import StringIO
from configparser import SectionProxy
import configparser

from csv2td import csv2td
from csv2td import filetemp



class CSV2TDTestCase(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        pass

    def tearDown(self):
        pass

    def test_import(self):
        self.assertTrue(True)

    """
    Test cases for correct_object_name
    """
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

    def test_name_not_str(self):
        with self.assertRaises(TypeError):
            r = csv2td.correct_object_name(1)

    def test_name_is_blank_str(self):
        with self.assertRaises(TypeError):
            r = csv2td.correct_object_name('')

    def test_guess_date_wrong_type(self):
        with self.assertRaises(AssertionError):
            r = csv2td.guess_date_format('somestr')

    def test_guess_date_yyyymmdd(self):
        input_dates = ['20160909','20170808']
        r = csv2td.guess_date_format(input_dates)
        self.assertEqual(r,'yyyymmdd')

    def test_guess_date_yyyy_mm_dd(self):
        input_dates = ['2016-09-09','2017-08-08']
        r = csv2td.guess_date_format(input_dates)
        self.assertEqual(r,'yyyy-mm-dd')

    def test_guess_date_ddmmyyyy2(self):
        input_dates = ['09/09/2018','31/12/2019']
        r = csv2td.guess_date_format(input_dates)
        self.assertEqual(r,'dd/mm/yyyy')

    def test_guess_date_ddmmyyyy3(self):
        input_dates = ['09-09-2018','31-12-2019']
        r = csv2td.guess_date_format(input_dates)
        self.assertEqual(r,'dd-mm-yyyy')

    def test_guess_date_none(self):
        input_dates = ['20160909','2017-08-08']
        r = csv2td.guess_date_format(input_dates)
        self.assertIsNone(r)

    """
    Test the get_config
    """
    def test_config_normal(self):
        text = filetemp.INI_FILE
        filename = filetemp.INI_FILE_NAME
        with open(filename,'w') as f:
            f.write(text)
        r = csv2td.get_config()
        self.assertTrue(isinstance(r, SectionProxy))
        os.remove(filename)

    def test_config_double_sections(self):
        text = filetemp.INI_FILE
        filename = filetemp.INI_FILE_NAME
        with open(filename,'w') as f:
            f.write(text)
            f.write(text)
        with self.assertRaises(configparser.DuplicateSectionError):
            r = csv2td.get_config()
        os.remove(filename)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CSV2TDTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
