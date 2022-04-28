import functools

from App.doc.code.test import spent_time


@functools.lru_cache()
def fib(num):
    if num in (1, 2):
        return 1
    return fib(num - 1) + fib(num - 2)


@spent_time('text')
def text(nums):
    for num in range(1, nums):
        print(f'{num}: {fib(num)}')


if __name__ == '__main__':
    # text(39)
    print(fib(99))