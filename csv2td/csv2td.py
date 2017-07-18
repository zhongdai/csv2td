# coding=utf-8

import csv
import pandas as pd
import numpy as np

from . import __version__


def command_line_runner():
    print('I am running, version is {}'.format(__version__))

if __name__ == '__main__':
    command_line_runner()
