import pytest
from commom.driver_factory import get_driver

@pytest.fixture(scope="funtion")
#scope表示每一个测试函数都会执行一次这个fixture
def driver():
    #为每一个测试函数都创建一个实例
    web_driver = get_driver()
    yield web_driver
    print("——————测试结束，关闭浏览器——————")
    web_driver.quit()