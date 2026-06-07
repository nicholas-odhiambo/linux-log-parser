#!/usr/bin/env python3

import argparse 
from datetime import datetime

parser = argparse.ArgumentParser(
    description="Linux Log Parser"
)

parser.add_argument(
    "--start-date",
    required=True,
    help="Start date (YYYY-MM-DD)"
)

parser.add_argument(
    "--end-date",
    required=True,
    help="End date (YYYY-MM-DD)"
)

args = parser.parse_args()

## date validation 
try:
    start_date = datetime.strptime(
        args.start_date,
        "%Y-%m-%d"
    )
    end_date = datetime.strptime(
        args.end_date,
        "%Y-%m-%d"
    )
except ValueError:
    print("Invalid date format. Use YYYY-MM-DD")
    exit(1)

## read log files 
try:
    with open("/var/log/cron", "r") as file:
        logs = file.readlines()
except FileNotFoundError:
    print('File not found')
    exit(1)