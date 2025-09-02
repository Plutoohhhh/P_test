import time

import pytest

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

@pytest.fixture(scope='session',autouse=True)
def timer_seesion_scope():
    star_time = time.time()
    print('\nstart:{}'.format(time.strftime(DATE_FORMAT,time.localtime(star_time))))

    yield

    finished = time.time()
    print('\nfinished:{}'.format(time.strftime(DATE_FORMAT,time.localtime(finished))))
    print('Total time cost:{:.3f}s'.format(finished - star_time))

@pytest.fixture(autouse=True)
def time_funtion_scope():
    start = time.time()
    yield
    print('Total time cost:{:.3f}s'.format(time.time() - start))

def test_1():
    time.sleep(1)


def test_2():
    time.sleep(2)

def loop():
    all = 0
    for i in range(10):
        i = i+1
        all = all + i

    print(all)

def loop_plus(n : int) -> int:
    all = 0
    for i in  range(1,n+1):
        all = all +i
    print(all)

def loop_plus2():
    i = 1
    all = 0
    while i <10:
        i = i+1
        all = all + i

    return all

if __name__ == '__main__':
    print(loop_plus2())






