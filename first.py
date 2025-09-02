import pytest


def test_fi():
    a = (1,2,3)
    b = (3,2,1)
    assert (2,2) == (2,2)
    assert 1 <= 2
    assert a != b

@pytest.mark.xfail
def test_sec():
    assert (132) <= (111)

@pytest.mark.skip(reason='')
def test_skip():
    assert 1 == 1

@pytest.mark.parametrize('passwd', ['12345678','asdasdasvcxvds','12345678910'])
def test_password(passwd):
    assert len(passwd) >= 10