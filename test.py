

a = '      '
import time
import datetime
def validCheck(date):
    date = date.strip()
    if len(date) != 10 or date[4] != '-' or date[7] != '-':
        return False
    check_string = date[:4] + date[5:7] + date[8:]
    for char in check_string:
        if not char.isdigit():
            return False
    print(date)
    try:
        time.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False



def calculate_date(initial_date, register_period):
    cur_date = [int(x) for x in initial_date.strip().split('-')]
    today = datetime.date.today()
    year = str(today.year)
    month = str(today.month).zfill(2)
    date = str(today.day - 1).zfill(2)
    return year + '-' + month + '-' + date



print(calculate_date('2017-08-06', '2'))