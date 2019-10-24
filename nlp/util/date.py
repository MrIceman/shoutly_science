import datetime


def convert_presse_time_to_ms(time):
    # time format is dd.mm.yyyy - HH:MM "06.08.2019 – 12:30"
    formatted_time = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S')
    return formatted_time.timestamp()


def timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)


def round_to_nearest_day(timestamp):
    time = timestamp_to_date(timestamp).timetuple()
    print(time)
    rounded_time = datetime.datetime(*time[0:3])
    print(rounded_time)
    return rounded_time.strftime('%d.%m')


def sort_reports_after_time(data, date_key, sort_function=None):
    if sort_function is not None:
        data.sort()
    return sorted(data, key=date_key)
