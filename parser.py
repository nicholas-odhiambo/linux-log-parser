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
    with open("sample_log.txt", "r") as file:
        logs = file.readlines()
except FileNotFoundError:
    print('File not found')
    exit(1)

## count log levels 
counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}
for line in logs: 
    timestamp = line[:19]
    log_date = datetime.strptime(
        timestamp,
        "%Y-%m-%d %H:%M:%S"
    )
    if start_date <= log_date <= end_date:
        if "INFO" in line:
            counts["INFO"] += 1
        elif "WARNING" in line:
            counts["WARNING"] +=1
        elif "ERROR" in line:
            counts["ERROR"] +=1

## generate report 
report =f"""
Linux Log summary report
========================

Date Range: 
{args.start_date} to {args.end_date}

INFO: {counts["INFO"]}
WARNING: {counts["WARNING"]}
ERROR: {counts["ERROR"]}
"""

with open ("report.txt", "w") as report_file:
    report_file.write(report)


print(report)
