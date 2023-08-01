# Library
from APILayer.API import APIOps


class ProductFunction(APIOps):
    name = ["XPATH", "//span[@class='base']"]
    price = ["XPATH", "/html[1]/body[1]/div[1]/main[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[1]/span[1]/span[2]/span[1]"]
    size = ["XPATH", "//div[@class='swatch-attribute size']//div[@role='listbox']"]
    allsize = ["CLASS_NAME", "swatch-option.text"]
    color = ["XPATH", "//div[@class='swatch-attribute color']//div[@role='listbox']"]
    allcolor = ["CLASS_NAME", "swatch-option.color"]
    main_image = ["CLASS_NAME", "fotorama__stage"]
    add_to_cart = ["CLASS_NAME", "action.primary.tocart"]
    qty_input = ["XPATH", "//input[@id='qty']"]

    def check_element_presence(self, element_name):
        if element_name == "username":
            return self.presence_of_element_located(self.name, 5)
        elif element_name == "main_image":
            return self.presence_of_element_located(self.main_image, 10)

    def get_product_name(self):
        return self.find_element(self.name).text

    def get_product_price(self):
        return self.find_element(self.price).text

    def get_all_available_sizes(self):
        return self.find_element(self.size)

    def get_all_available_size_text(self, obj):
        return self.find_elements_by_object(obj,self.allsize)

    def get_all_available_color(self):
        return self.find_element(self.color)

    def get_all_available_color_text(self, obj):
        return self.find_elements_by_object(obj,self.allcolor)

    def open_url_to_navigate(self, TestData):
        self.open_url(TestData['url'])

    def get_color_hex_value(self,rgb):
        return self.get_hex_value_color(rgb)

    def select_sort_drop_down_elem(self):
        return self.select_sort_drop_down(self.allsize)

    def get_add_to_cart_button(self):
        return self.find_element(self.add_to_cart)

    def is_add_to_cart_button_clickble(self):
        return self.find_element(self.add_to_cart).get_property('disabled')

    def set_product_quantities(self, qty):
        elem = self.find_element(self.qty_input)
        elem.clear()
        elem.send_keys(qty)
