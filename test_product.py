import time
import allure
import pytest

from test.product_selection import ProductFunction
from my_yaml.pytestyaml import *
from tools.logs import LogInformation
import inspect


@allure.description("test_product_information : This test select the product from the product catalog")
def test_product_information(driver):
    functionname = inspect.currentframe().f_code.co_name
    loggingData = LogInformation(namefile=functionname)
    loggingData.TEST_INFORMATION(namefile=functionname, message="Class Name - " + functionname)
    yamlconfig = "config_pytest"

    product = ProductFunction(driver)

    TestData = readyaml(functionname, yamlconfig)
    loggingData.TEST_INFORMATION(namefile=functionname, message="url - " + TestData['url'])
    product.open_url_to_navigate(TestData)

    bPresence = product.check_element_presence("main_image")

    if bPresence is True:
        assert TestData['url'] == driver.current_url
        get_product_name = product.get_product_name()
        assert TestData['name'] == get_product_name
        loggingData.TEST_INFORMATION(namefile=functionname, message="get_product_name - " + get_product_name)
        get_product_price = product.get_product_price()
        assert TestData['price'] == get_product_price
        loggingData.TEST_INFORMATION(namefile=functionname, message="get_product_price - " + get_product_price)
        list_size = []
        get_all_available_sizes = product.get_all_available_sizes()
        get_all_available_size_text = product.get_all_available_size_text(get_all_available_sizes)
        for obj in get_all_available_size_text:
            list_size.append(obj.text)
            loggingData.TEST_INFORMATION(namefile=functionname, message="get_all_available_sizes - " + obj.text)
        assert TestData['size'] == list_size
        get_product_color = product.get_all_available_color()
        get_product_color_text = product.get_all_available_color_text(get_product_color)
        list_color = []
        for obj in get_product_color_text:
            list_color.append(product.get_color_hex_value(obj.value_of_css_property('background-color')))
            loggingData.TEST_INFORMATION(namefile=functionname,
                                         message="get_product_color_text - " + product.get_color_hex_value(
                                             obj.value_of_css_property('background-color')))
        assert TestData['color'] == list_color


def test_all_items_in_cart(driver):
    functionname = inspect.currentframe().f_code.co_name
    loggingData = LogInformation(namefile=functionname)
    loggingData.TEST_INFORMATION(namefile=functionname, message="Class Name - " + functionname)
    yamlconfig = "config_pytest"

    product = ProductFunction(driver)

    TestData = readyaml(functionname, yamlconfig)

    get_all_available_sizes = product.get_all_available_sizes()
    get_all_available_size_text = product.get_all_available_size_text(get_all_available_sizes)

    get_product_color = product.get_all_available_color()
    get_product_color_text = product.get_all_available_color_text(get_product_color)

    for size in get_all_available_size_text:
        if size.text == "XS":
            size.click()
            for obj in get_product_color_text:
                if "#000000" == product.get_color_hex_value(obj.value_of_css_property('background-color')):
                    obj.click()
                    product.set_product_quantities(TestData['S'])
                    if product.is_add_to_cart_button_clickble() == False:
                        product.get_add_to_cart_button().click()

    #sortdropdown = product.select_sort_drop_down_elem()
    #sortdropdown.select_by_visible_text('XS')

    time.sleep(10)


