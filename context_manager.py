import time
from contextlib import contextmanager

'''
First implementation - a class-based context manager.
'''


class TimeIt:

    def __init__(self):
        self.start_time = 0
        self.stop_time = 0

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_time = time.time()
        print(f"Program execution time: {self.stop_time - self.start_time}")


'''
Second implementation - a decorator-based context manager
'''


@contextmanager
def time_program():
    try:
        start_time = time.time()
        yield start_time
    finally:
        end_time = time.time()
        print(f"Program execution time: {end_time - start_time}")


def test1():
    print("running test 1 - class based context manager")
    with TimeIt() as t:
        # kill some time here
        for _ in range(10000):
            a = 100 ** 10000


def test2():
    print("running test 2 - decorator based context manager")
    with time_program() as t:
        # kill some time here
        for _ in range(10000):
            a = 100 ** 10000


if __name__ == '__main__':
    test1()
    test2()
