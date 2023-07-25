from test.login_page import FormAuthentication
from yaml.pytestyaml import *
from tools.logs import LogInformation

def test_form_authentication(driver):
    functionname = inspect.currentframe().f_code.co_name
    loggingData = LogInformation(namefile=functionname)
    loggingData.TEST_INFORMATION(namefile=functionname, message="Class Name - " + functionname) 
    yamlconfig="config_pytest"
  
    form = FormAuthentication(driver)
    
    TestData = readyaml(functionname, yamlconfig)    
    loggingData.TEST_INFORMATION(namefile=functionname, message="url - " + TestData['url'])    
    form.open_url_to_navigate(TestData)
    assert TestData['url'], driver.current_url
  
    bPresence = form.check_element_presence("username")
    if bPresence is true:
        form.enter_username(TestData)
        loggingData.TEST_INFORMATION(namefile=functionname, message="username - " + TestData['username'])
        form.enter_password(TestData)
        loggingData.TEST_INFORMATION(namefile=functionname, message="password - " + TestData['password'])
  
        form.press_submit_button()

        bPresence = form.check_element_presence("mainmenu")
        
        if bPresence is true:
            actualUrl = driver.current_url
            expectedUrl = TestData['expected']
            assert expectedUrl, actualUrl
            loggingData.TEST_INFORMATION(namefile=functionname, message="expectedUrl - " + expectedUrl)
            loggingData.TEST_INFORMATION(namefile=functionname, message="actualUrl - " + actualUrl)  
        else:
            loggingData.TEST_INFORMATION(namefile=functionname, message="main menu took too much time to load")
    else:
        loggingData.TEST_INFORMATION(namefile=functionname, message="username took too much time to load")
            
    loggingData.TEST_INFORMATION(namefile=functionname, message="*******End test - test_check_login********")
