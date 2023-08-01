# Library
from APILayer.API import APIOps


class SearchPageFunction(APIOps):
    searchelem = ["ID", "search"]
    sortdropdown = ["ID", "sorter"]
    sortdropdownelem = ["TAG_NAME", "option"]
    elemname = ["CLASS_NAME", "qs-option-name"]
    amount = ["CLASS_NAME", "amount"]
    allsearchedresult = ["CLASS_NAME", "products.list.items.product-items"]
    productinfo = ["TAG_NAME", "li"]
    itemname = ["CLASS_NAME", "product.name.product-item-name"]


    def open_url_to_navigate(self, TestData):
        self.open_url(TestData['url'])

    def search_element(self):
        return self.find_element(self.searchelem)

    def presence_of_element(self):
        self.presence_of_element_located(self.sortdropdown, timeout=10)

    def select_sort_drop_down_elem(self):
        return self.select_sort_drop_down(self.sortdropdown)

    def get_all_search_items(self):
        return self.find_element(self.allsearchedresult)

    def get_all_product_info(self, obj):
        return self.find_elements_by_object(obj, self.productinfo)

    def get_item_name(self, obj):
        return self.find_element_by_object(obj,self.itemname).text

    def set_key_send(self, obj):
        self.set_send_key(obj)