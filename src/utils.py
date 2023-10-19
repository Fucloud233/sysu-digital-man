from datetime import datetime


def cal_time(begin: datetime, end: datetime):
    sub_time = end - begin
    return "%02d.%d"%(sub_time.seconds, sub_time.microseconds)


def __test():
    begin = datetime.now()

    count = 100000000
    while count>0:
        count -= 1

    end = datetime.now()

    print(cal_time(begin, end))

if __name__ == '__main__':
    __test()