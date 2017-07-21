# coding=utf-8

import csv
import os
import argparse
import configparser
import pandas as pd
import numpy as np
import re

from . import __version__
from .filetemp import INI_FILE, INI_FILE_NAME, FASTLOAD_CTL
from .filetemp import INI_FILE_KEYS

def correct_object_name(object_name):
    """
    Make sure the field name is valid in Teradata, this is also for table name
    - No more than 32 characters
    - Not start with numeric
    - No speical characters
    - No spaces
    """
    if not isinstance(object_name, str) or len(object_name) == 0:
        raise TypeError('Please make sure the field_name is a str and not null')

    MAX_LENGTH = 30
    REGEX = re.compile(r"[^a-zA-Z0-9]")
    no_special_chars = REGEX.sub('_', object_name)
    if re.match(r"\d+", no_special_chars) is not None:
        no_special_chars = '_' + no_special_chars

    return no_special_chars[:MAX_LENGTH]

def guess_date_format(list_of_date):
    """
    Check the format for a date string, return one of following
    yyyymmdd
    yyyy-mm-dd
    dd/mm/yyyy
    ddmmyyyy
    dd-mm-yyyy

    or return None if not match any
    """
    assert isinstance(list_of_date,list)
    matchers = {
        'yyyymmdd':re.compile(r"\d{4}[0|1]\d[0|1|2|3]\d"),
        'yyyy-mm-dd':re.compile(r"\d{4}\-[0|1]\d\-[0|1|2|3]\d"),
        'dd/mm/yyyy':re.compile(r"[0|1|2|3]\d\/[0|1]\d\/\d{4}"),
        'dd-mm-yyyy':re.compile(r"[0|1|2|3]\d\-[0|1]\d\-\d{4}")
    }
    return_format = None
    for name, m in matchers.items():
        for item in list_of_date:
            if m.match(item) is None:
                # if found any not matching (in the middle), set to None
                # and break the inner loop
                return_format = None
                break
            else:
                return_format = name

        # if we matched to any format, just break the outer loop
        if return_format is not None:
            break
    return return_format

class CSVField:
    def __init__(self, name,
                 dtype=None,
                 min_len=None,
                 max_len=None,
                 date_format=None):
        assert isinstance(name, str)

        self.name = name
        self.dtype = dtype
        self.min_len = min_len
        self.max_len = max_len
        self.date_format = date_format

    def __repr__(self):
        return 'CSVField({})'.format(self.name)




def get_parser():
    parser = argparse.ArgumentParser(description='Generate Fastload script')

    parser.add_argument('filename',type=str,
                        help='The filename of CSV file to be loaded to Teradata')

    return parser

def get_config():
    cfg = configparser.ConfigParser()
    error_message = """
    The configuration file name should be csv2td.ini, please make sure it has all
    required format / data.
    Please execute `csv2tdinit` to generate a template file under same folder.
    """
    try:
        cfg.read(INI_FILE_NAME)
    except Exception as e:
        raise

    sections = cfg.sections()
    if len(sections) != 1:
        raise SystemExit(error_message)

    section_name = sections[0]

    for key in INI_FILE_KEYS:
        if key not in cfg[section_name]:
            raise SystemExit(error_message)
    return cfg[section_name]

def generate_init_file():
    current_dir = os.getcwd()

    with open(os.path.join(current_dir, INI_FILE_NAME), 'w') as f:
        f.write(INI_FILE)

    print('The template configuration file [{}] has been generated at current folder'.format(INI_FILE_NAME))
    return

def command_line_runner():
    parser = get_parser()

    args = vars(parser.parse_args())

    # File only can be placed under the current folder
    csv_filename = args['filename']
    full_path = os.path.join(os.getcwd(),csv_filename)

    if not os.path.isfile(full_path):
        raise ValueError('{} is not a file, please check'.format(full_path))

    s = csv.Sniffer()
    with open(full_path) as f:
        if not s.has_header(f.read(1024)):
            has_header = False
        else:
            has_header = True
    if not has_header:
        raise ValueError('please make sure you have headers in the file')

    # Get the config object
    section = get_config()

    # process data




if __name__ == '__main__':
    command_line_runner()
