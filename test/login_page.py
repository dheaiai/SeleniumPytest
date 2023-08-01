# Library
from APILayer.API import APIOps


class FormAuthentication(APIOps):
    username = ["NAME", "login[username]"]
    password = ["NAME", "login[password]"]
    SubmitBtn = ["ID", "send2"]
    mainmenu = ["CLASS_NAME", "ui.nav.items"]

    def check_element_presence(self, element_name):
        if element_name == "username":
            return self.presence_of_element_located(self.username, 5)
        elif element_name == "mainmenu":
            return self.presence_of_element_located(self.mainmenu, 10)

    def enter_username(self, TestData):
        username_textbox = self.find_element(self.username)
        username_textbox.send_keys(TestData['username'])

    def enter_password(self, TestData):
        password_textbox = self.find_element(self.password)
        password_textbox.send_keys(TestData['password'])

    def press_submit_button(self):
        SignIn_button = self.find_element(self.SubmitBtn)
        SignIn_button.submit()

    def open_url_to_navigate(self, TestData):
        self.open_url(TestData['url'])
