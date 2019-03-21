
from datetime import datetime

'''
Program to sort given dates in string format.
'''


def sort_dates(dates_list):
   dates_list.sort(key=lambda date: datetime.strptime(date, '%d %b %Y'))
   return dates_list


if __name__ == '__main__':
    dates = ["23 Jun 2018", "2 Dec 2017", "11 Jun 2018",
             "01 Jan 2019", "10 Jul 2016", "01 Jan 2007"]

    print('Sorted dates are', sort_dates(dates));
