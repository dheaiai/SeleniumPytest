import time

import pytest
from selenium.webdriver import Keys

from test.login_page import FormAuthentication
from test.search_function import SearchFunction
from test.search_page import SearchPageFunction
from my_yaml.pytestyaml import *
from tools.logs import LogInformation
import inspect





@pytest.mark.only
def test_form_search_page(driver):
    functionname = inspect.currentframe().f_code.co_name
    yamlconfig = "config_pytest"

    form = SearchPageFunction(driver)

    TestData = readyaml(functionname, yamlconfig)
    form.open_url_to_navigate(TestData)
    assert TestData['url'], driver.current_url

    searchelement = form.search_element()
    searchelement.send_keys(TestData['searchFor'])
    searchelement.send_keys(Keys.RETURN)
    form.presence_of_element()
    sortdropdown = form.select_sort_drop_down_elem()
    sortdropdown.select_by_visible_text('Price')


