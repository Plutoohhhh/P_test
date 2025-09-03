from selenium import webdriver
from page_objects.baidu_page import BaiduPage
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService



def test_baidu_pom():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.baidu.com")
    baidu_page = BaiduPage(driver)
    search_term = "嘎嘎"
    baidu_page.search_for(search_term)

    time.sleep(3)
    assert search_term in baidu_page.get_title()
    driver.quit()