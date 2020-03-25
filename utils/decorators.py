import datetime

from django.db import reset_queries, connection



def check_speed(func):
    """
    Декоратор для подсчета кол-ва запросов в БД и времени их выполнения + время ввыполнения самой функции
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        # Перед выполнение функции
        reset_queries()
        now_queries = len(connection.queries)
        time_now = datetime.datetime.now()
        # Выполнение финкции
        result = func(*args, **kwargs)
        # После выполнения  функции
        func_name = func.__name__
        time_diff = str(datetime.datetime.now() - time_now)
        queries_count = len(connection.queries) - now_queries
        times = round(sum([float(x.get('time')) for x in connection.queries]), 3)
        print('check_speed:{} (time:{} queries:{} sql_time:{})'.format(func_name, time_diff, queries_count, str(times)))
        return result
    return wrapper
