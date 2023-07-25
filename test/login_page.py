# Library
from APILayer.API import *

class FormAuthentication(CommonOps):
  
    username = ["NAME", "login[username]"]
    password = ["NAME", "login[password]"]
    SubmitBtn = ["ID", "send2"]
    mainmenu = ["CLASS_NAME", "ui.nav.items"]

    def check_element_presence(self, username, timeout):
        return presence_of_element_located(username, timeout)
      
    def enter_username(self, username, TestData)  
      username_textbox = find_element(username)
      username_textbox.send_keys(TestData['username'])

    def enter_password(self, password, TestData)
      password_textbox = find_element(password)
      password_textbox.send_keys(TestData['password'])

    def press_submit_button(SubmitBtn)
      SignIn_button = find_element(SubmitBtn)
      SignIn_button.submit()
