import selenium
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#ByID,By.CSS_SELECTOR,By.XPATH
#ByNAME,ByCLASS_NAME,By.TAG_NAME,By.LINK_TEXT,By.PARTIAL_LINK_TEXT
#共8种，前三种较常用，但是XPATH表达式编写较难

@pytest.fixture()
def web_url():
    return "https://www.baidu.com"

def test_open_baidu(web_url):
    driver = webdriver.Chrome

    driver.get(web_url)
    page_title = driver.title
    print(f"当前页面的标题是：{page_title}")
    assert "百度" in page_title
    time.sleep(3)
    driver.quit()

def test_baidu_search(web_url):
    #1.打开浏览器
    #2.打开百度
    #3.定位搜索框和搜索按钮元素
    #4.输入内容到搜索框
    #5.点击搜索按钮
    #6.判断是否成功
    #7.关闭浏览器
    driver = webdriver.Chrome
    driver.get(web_url)
    wait =WebDriverWait(driver,10)
    search_box = wait.until(EC.visibility_of_element_located((By.ID,"kw")))
    search_box.send_keys("自动化")
    search_button = wait.until(EC.element_to_be_clickable((By.ID,"su")))
    search_button.click
    wait.until(EC.title_contains("自动化"))
    assert "自动化" in driver.title
    driver.quit