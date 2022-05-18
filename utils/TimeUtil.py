import datetime


class TimeUtil:
    # 判断是否收盘
    @staticmethod
    def is_close_time():
        close_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '15:00', '%Y-%m-%d%H:%M')
        # 当前时间
        n_time = datetime.datetime.now()
        return n_time >= close_time
