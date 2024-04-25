from datetime import datetime


def time_measure(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print(f"Function started: {start}")
        result = func(*args, **kwargs)
        finish = datetime.now()
        print(f"Function stopped: {finish}")
        func_time = (finish - start).total_seconds()
        print(f"Function time: {func_time}")
        return result
    return wrapper


@time_measure
def multiply_num(num_1, num_2):
    return num_1 * num_2

multiply_num(3, 5)