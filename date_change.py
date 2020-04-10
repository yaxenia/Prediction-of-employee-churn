import datetime as dt


def date_change(str_date):   # changes date to a time format from a given date in seconds

    start_date = dt.datetime(2019, 1, 1, 0, 0)  # given date : 01.01.2019

    try:
        date = dt.datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(' conversion error ')
    else:

        transformed_date = (date - start_date).total_seconds()
        print(transformed_date)
