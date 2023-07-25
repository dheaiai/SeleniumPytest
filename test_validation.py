import time

from test.login_page import FormAuthentication
from test.search_function import SearchFunction
from my_yaml.pytestyaml import *
from tools.logs import LogInformation
import inspect


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
