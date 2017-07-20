# csv2td
[![Build Status](https://travis-ci.org/travis-ci/travis-web.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web) [![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
---
A simple script to generate [Teradata](http://www.teradata.com/) `fastload` control file from a CSV file


## Installation
Required Python packages:
- pandas >= 0.19.2
- numpy >= 1.11.3

## Usage

## Features
- Generate the `fastload` control file based on a given CSV file
- Define the table structure by guessing the format of CSV columns
> `fastload` only load to new tables without any existing records, so there is no append mode

## License
MIT
