from test.login_page import FormAuthentication

def test_form_authentication(driver):
  
    form = FormAuthentication(driver)

    form.open_url_to_navigate(TestData)
    form.check_element_presence("username")
    form.enter_username(TestData)
    form.enter_password(TestData)
    form.press_submit_button()

    assert "logged in" in form.check_login_logout_status().text 

    form.click_logout_button()
    assert "logged out" in form.check_login_logout_status().text
