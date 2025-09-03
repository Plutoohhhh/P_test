import selenium
from selenium import webdriver
import time

def test_open_baidu():
    driver = webdriver.chrome()

    driver.get("https://www.baidu.com")
    page_title = driver.title
    print(f"当前页面的标题是：{page_title}")
    assert "百度" in page_title
    time.sleep(3)
    driver.quit()