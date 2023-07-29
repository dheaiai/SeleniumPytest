import time
import allure
import pytest
from selenium.webdriver import Keys

from test.login_page import FormAuthentication
from test.search_function import SearchFunction
from test.search_page import SearchPageFunction
from my_yaml.pytestyaml import *
from tools.logs import LogInformation
import inspect


@allure.description("test_form_authentication : This test check the login functionality with correct credentials")
@pytest.mark.forallure
def test_form_authentication(driver):
    functionname = inspect.currentframe().f_code.co_name
    loggingData = LogInformation(namefile=functionname)
    loggingData.TEST_INFORMATION(namefile=functionname, message="Class Name - " + functionname)
    yamlconfig = "config_pytest"

    form = FormAuthentication(driver)

    TestData = readyaml(functionname, yamlconfig)
    loggingData.TEST_INFORMATION(namefile=functionname, message="url - " + TestData['url'])
    form.open_url_to_navigate(TestData)
    assert TestData['url'], driver.current_url

    bPresence = form.check_element_presence("username")
    if bPresence is True:
        form.enter_username(TestData)
        loggingData.TEST_INFORMATION(namefile=functionname, message="username - " + TestData['username'])
        form.enter_password(TestData)
        loggingData.TEST_INFORMATION(namefile=functionname, message="password - " + TestData['password'])

        form.press_submit_button()

        bPresence = form.check_element_presence("mainmenu")

        if bPresence is True:
            actualUrl = driver.current_url
            expectedUrl = TestData['expected']
            assert expectedUrl, actualUrl
            loggingData.TEST_INFORMATION(namefile=functionname, message="expectedUrl - " + expectedUrl)
            loggingData.TEST_INFORMATION(namefile=functionname, message="actualUrl - " + actualUrl)
        else:
            loggingData.TEST_INFORMATION(namefile=functionname, message="main menu took too much time to load")
    else:
        loggingData.TEST_INFORMATION(namefile=functionname, message="username took too much time to load")


def test_form_search(driver):
    functionname = inspect.currentframe().f_code.co_name
    loggingData = LogInformation(namefile=functionname)
    loggingData.TEST_INFORMATION(namefile=functionname, message="Class Name - " + functionname)
    yamlconfig = "config_pytest"

    form = SearchFunction(driver)

    TestData = readyaml(functionname, yamlconfig)
    loggingData.TEST_INFORMATION(namefile=functionname, message="url - " + TestData['url'])
    form.open_url_to_navigate(TestData)
    assert TestData['url'], driver.current_url

    bPresence = form.check_element_presence("username")
    if bPresence is True:
        form.enter_username(TestData)
        loggingData.TEST_INFORMATION(namefile=functionname, message="username - " + TestData['username'])
        form.enter_password(TestData)
        loggingData.TEST_INFORMATION(namefile=functionname, message="password - " + TestData['password'])

        form.press_submit_button()

        bPresence = form.check_element_presence("mainmenu")

        if bPresence is True:
            actualUrl = driver.current_url
            expectedUrl = TestData['expected']
            assert expectedUrl, actualUrl
            loggingData.TEST_INFORMATION(namefile=functionname, message="expectedUrl - " + expectedUrl)
            loggingData.TEST_INFORMATION(namefile=functionname, message="actualUrl - " + actualUrl)
        else:
            loggingData.TEST_INFORMATION(namefile=functionname, message="main menu took too much time to load")
    else:
        loggingData.TEST_INFORMATION(namefile=functionname, message="username took too much time to load")

    searchelement = form.search_element()
    searchelement.send_keys(TestData['searchFor'])
    time.sleep(5)
    searchresult = form.search_result()
    elementslist = form.element_list(searchresult)
    elem_dict = {}
    for opt in elementslist:
        mytext = form.get_search_result_text(opt)
        amounttext = form.get_search_result_amount(opt)
        elem_dict.update({mytext: amounttext})
        loggingData.TEST_INFORMATION(namefile=functionname, message=mytext + ":" + amounttext)
    elem_dict = {TestData['searchFor']: elem_dict}
    loggingData.TEST_INFORMATION(namefile=functionname, message=elem_dict)
    writeyaml(elem_dict,"search_data")
    time.sleep(10)
    loggingData.TEST_INFORMATION(namefile=functionname, message="*******End test - test_check_login********")


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
    sortdropdown.select_by_visible_text('Product Name')
    time.sleep(5)
    allsearchitems = form.get_all_search_items()
    allproductinfo = form.get_all_product_info(allsearchitems)
    itemnames = []
    for obj in allproductinfo:
        itemnames.append(form.get_item_name(obj))

    sorted = all(a <= b for a, b in zip(itemnames[1:], itemnames))
    assert sorted, True

