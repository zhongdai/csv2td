# coding=utf-8

import csv
import pandas as pd
import numpy as np
import re

from . import __version__

def correct_object_name(object_name):
    """
    Make sure the field name is valid in Teradata, this is also for table name
    - No more than 32 characters
    - Not start with numeric
    - No speical characters
    - No spaces
    """
    if not isinstance(object_name, str):
        raise TypeError('Please make sure the field_name is a str')

    MAX_LENGTH = 30
    REGEX = re.compile(r"[^a-zA-Z0-9]")
    no_special_chars = REGEX.sub('_', object_name)
    if re.match(r"\d+", no_special_chars) is not None:
        no_special_chars = '_' + no_special_chars

    return no_special_chars[:MAX_LENGTH]




def command_line_runner():
    print('I am running, version is {}'.format(__version__))

if __name__ == '__main__':
    command_line_runner()
