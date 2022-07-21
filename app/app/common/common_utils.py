from datetime import datetime, date
import pytz


def now():
    return datetime.now(pytz.timezone('Asia/Tokyo'))


def convert_date_from_str(date_str: str)->date:
    tstr = '{date} 00:00:00'.format(date = date_str)
    tdatetime = datetime.strptime(tstr, '%Y/%m/%d %H:%M:%S')
    tdate = date(tdatetime.year, tdatetime.month, tdatetime.day)
    return tdate