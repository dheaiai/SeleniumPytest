ame_# Library
from APILayer.API import APIOps

class FormAuthentication(APIOps):
  
    username = ["NAME", "login[username]"]
    password = ["NAME", "login[password]"]
    SubmitBtn = ["ID", "send2"]
    mainmenu = ["CLASS_NAME", "ui.nav.items"]

    def check_username_presence(self, username, timeout):
        return self.presence_of_element_located(username, timeout)
      
    def enter_username(self, username, TestData)  
        username_textbox = self.find_element(username)
        username_textbox.send_keys(TestData['username'])

    def enter_password(self, password, TestData)
        password_textbox = self.find_element(password)
        password_textbox.send_keys(TestData['password'])

    def press_submit_button(self, SubmitBtn)
        SignIn_button = self.find_element(SubmitBtn)
        SignIn_button.submit()
      
    def open_url_no_navigate(self, TestData)
        open_url(TestData['url'])
