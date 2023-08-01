# Library
from APILayer.API import APIOps


class SearchFunction(APIOps):
    username = ["NAME", "login[username]"]
    password = ["NAME", "login[password]"]
    SubmitBtn = ["ID", "send2"]
    mainmenu = ["CLASS_NAME", "ui.nav.items"]
    searchelem = ["ID", "search"]
    list = ["ID", "search_autocomplete"]
    listelem = ["TAG_NAME", "li"]
    elemname = ["CLASS_NAME", "qs-option-name"]
    amount = ["CLASS_NAME", "amount"]

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

    def search_element(self):
        return self.find_element(self.searchelem)

    def search_result(self):
        return self.find_element(self.list)

    def element_list(self, obj):
        return self.find_elements_by_object(obj, self.listelem)

    def get_search_result_text(self,obj):
        return self.find_element_by_object(obj, self.elemname).text

    def get_search_result_amount(self,obj):
        return self.find_element_by_object(obj, self.amount).text


