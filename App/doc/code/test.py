import functools
import time


def spent_time(text):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            t = time.time()
            ret = fn(*args, **kwargs)
            spent = time.time() - t
            print("程序运行花费时间{},参数{}".format(spent, text))
            return ret
        return wrapper
    return decorator


@spent_time('good')
def test(hello):
    print("%s I'm here, pls help me" % hello)
    time.sleep(3)


if __name__ == '__main__':
    test('xiaoming')
    print(test.__name__)
