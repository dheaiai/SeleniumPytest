from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class APIOps:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)
        self._action = ActionChains(self.driver)
        
    def by_locator(self, byclass):
        if byclass == "NAME":
            return By.NAME
        elif byclass == "ID":
            return By.ID
        elif byclass == "CLASS_NAME":
            return By.CLASS_NAME
        elif byclass == "XPATH":
            return By.XPATH
        elif byclass == "TAG_NAME":
            return By.TAG_NAME    
    
    def presence_of_element_located(self, element, timeout):
        try:
            element_present = EC.presence_of_element_located((self.by_locator(element[0]), element[1]))
            WebDriverWait(self.driver, timeout).until(element_present)
            return True
        except TimeoutException:
            return False

    def find_element(self, element):
        return self.driver.find_element(self.by_locator(element[0]), element[1])

    def find_elements(self, element):
        return self.driver.find_elements(self.by_locator(element[0]), element[1])
       
    def web_driver(self):
        return webdriver.Chrome()
        
    def open_url(self, url):
        self.driver.get(url)

    def find_element_by_object(self, obj, element):
        return obj.find_element(self.by_locator(element[0]), element[1])

    def find_elements_by_object(self, obj, element):
        return obj.find_elements(self.by_locator(element[0]), element[1])

    def select_sort_drop_down(self,element):
        return Select(self.driver.find_element(self.by_locator(element[0]), element[1]))