import datetime


class DateUtil:
    @staticmethod
    def today():
        return datetime.datetime.strptime(str(datetime.datetime.now().date()), '%Y-%m-%d')
