from selenium import webdriver
from page_objects.baidu_page import BaiduPage
import time

def test_baidu_pom():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    baidu_page = BaiduPage(driver)
    search_term = "Page"
    baidu_page.search_for(search_term)

    time.sleep(3)
    assert search_term in baidu_page.get_title()
    driver.quit()