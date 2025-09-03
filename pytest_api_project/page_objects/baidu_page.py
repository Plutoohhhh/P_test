from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaiduPage:
    Search_box = (By.ID,"kw")
    Click_button = (By.ID,"su")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
    def search_for(self,text):
        search_box_element = self.wait.until(EC.visibility_of_element_located(self.Search_box))
        search_box_element.sent_keys(text)
        search_button_element = self.wait.until(EC.element_to_be_clickable(self.Click_button))
        search_button_element.click()

    def get_title(self):
        return self.driver.title