"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""
import calendar
from datetime import datetime, date, timedelta

def print_days():
    dt_now = datetime.now()
    print(dt_now.strftime('%d.%m.%Y'))
    
    dt_yesterday = datetime.now() - timedelta(1)
    print(dt_yesterday.strftime('%d.%m.%Y'))

    date = datetime.now()
    days_in_month = calendar.monthrange(date.year, date.month)[1]
    date = date - timedelta(days=days_in_month)
    print(date.strftime('%d.%m.%Y'))
    

def str_2_datetime(string):
    input(string).strftime('%d/%m/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))