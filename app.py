import argparse
import datetime
import zoneinfo
from dateutil.relativedelta import relativedelta
from zoneinfo import ZoneInfo
import re
import sys

def change_timezone(timestamp, timezone1):
    return timestamp.astimezone(timezone1)


def run(args):

    t1_utc = None
    t2_utc = None

    # Parse arguments to make sure they're in the correct format.
    # ---------------------------------------------------------------------
    if args.tz not in zoneinfo.available_timezones():
        raise Exception("ERROR: Timezone not found")
    elif re.match("1[hdy]$|1mo$", args.period) is None:
        # Locates '1' followed by 'h' or 'd' or 'y' or 'mo' and end of line. 
        raise Exception("ERROR: Period not applicable")
    elif re.match("\d{8}T\d{6}Z", args.t1) is None:
        # t1 must be in the correct format.
        raise Exception("ERROR: t1 not formatted correctly")
    elif re.match("\d{8}T\d{6}Z", args.t2) is None:
        # t2 must be in the correct format.
        raise Exception("ERROR: t2 not formatted correctly")
    else:
        # t2 must be in the future with respect to t1.
        t1 = args.t1
        t1_r = t1.replace("Z", "").replace("T", "")
        t1_utc = datetime.datetime.strptime(t1_r, "%Y%m%d%H%M%S").replace(
            tzinfo=ZoneInfo("UTC")
        )

        t2 = args.t2
        t2_r = t2.replace("Z", "").replace("T", "")
        t2_utc = datetime.datetime.strptime(t2_r, "%Y%m%d%H%M%S").replace(
            tzinfo=ZoneInfo("UTC")
        )

        if t2_utc < t1_utc:
            raise Exception("ERROR: t1 > t2")
    # ---------------------------------------------------------------------

    timezone = ZoneInfo(args.tz)

    supported_periods = ["y", "mo", "d", "h"]
    kwargs_periods = ["years", "months", "days", "hours"]

    period_index = supported_periods.index(args.period[1:])

    # Period dict : Used to round the timestamps to the start of each periodic event. Will round to:
    #    period=d:  the nearest day in the past.
    #    period=mo: the nearest month in the past.
    #    period=y:  the nearest year in the past.
    period_dict = {k: (1 if i>=period_index else 0) for i,k in enumerate(supported_periods)}

    # Arguments for the timeshift == period of the event.
    kwargs = {k: (1 if i == period_index else 0) for i, k in enumerate(kwargs_periods)}

    t1_local = change_timezone(t1_utc, timezone)
    t2_local = change_timezone(t2_utc, timezone)

    print(f'Timestamp t1 {t1_utc}')
    print(f'Timestamp t2 {t2_utc}')

    # Independent of the period -> round to nearest hour in the past.
    dt1 = relativedelta(minutes=t1_utc.minute, seconds=t1_utc.second)

    # Dependent on the period (d, mo, y). Round to the start of each periodic event.
    dt2 = relativedelta(
        months=period_dict["y"] * (t1_local.month - 1),
        days=period_dict["mo"] * (t1_local.day - 1),
        hours=period_dict["d"] * t1_local.hour,
    )

    t1_local = t1_local - dt1 - dt2

    timestamps_local = []
    timestamps_utc = []


    # Shift t1_local by the period until it reaches t2_local.
    # Convert to UTC and append to list.
    while t1_local < t2_local:
        t1_local += relativedelta(**kwargs)

        timestamps_local.append(t1_local)
        timestamps_utc.append(change_timezone(t1_local, ZoneInfo("UTC")))


    # Drop last element as it has surpassed t2_local.
    timestamps_local = timestamps_local[:-1]
    timestamps_utc = timestamps_utc[:-1]

    # Format timestamps from datetime to string.
    timestamps_utc_formatted = [
        timestamp.strftime("%Y%m%dT%H%M%SZ") for timestamp in timestamps_utc
    ]

    print('Timestamps between t1 and t2')
    for timestamp in timestamps_utc_formatted:
        print(timestamp)

    return timestamps_utc_formatted




if __name__ == '__main__':

    # Command line argument parser.
    parser = argparse.ArgumentParser(description="Description")

    parser.add_argument("--period", type=str, help="Period")
    parser.add_argument("--tz", type=str, help="Timezone")
    parser.add_argument("--t1", type=str, help="Start of periodic event")
    parser.add_argument("--t2", type=str, help="End of periodic event")

    args = parser.parse_args()
    # print(args)
    
    try:
        run(args = args)
    except Exception as e:
        print(e)
        sys.exit(10)
