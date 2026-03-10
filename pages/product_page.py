import time
from urllib.parse import parse_qs, urlparse

from selenium.webdriver.common.by import By

from selenium_main_project.SeleniumMainProject.pages.base_page import BasePage
from selenium_main_project.SeleniumMainProject.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        self.click_to_add_to_basket_button()
        self.solve_quiz_and_get_code()#вычисление математического выражения
        self.should_be_massage_about_add_to_basket(self.get_product_name())
        self.should_be_message_about_basket_cost(self.get_product_cost())

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), \
            "Сообщение об успешном добавлении появилось, хотя не должно было"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), \
            "Сообщение об успешном добавлении не исчезло"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), \
            "Конпка добавления товара в корзину не найдена"

    def click_to_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()

    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.H1), \
            "Название товара не найдено"
        return self.browser.find_elements(*ProductPageLocators.H1)[-1].text

    def get_product_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), \
            "Цена товара не найдена"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text

    def should_be_massage_about_add_to_basket(self, product_name):
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS), \
            "Сообщение об успешном добавлении товара не найдено"

        message = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS).text
        assert product_name == message, f"В сообщении, об успешном добавлении, не содержится имя товара. Имя товара {product_name}, Сообщение {message}"

    def should_be_message_about_basket_cost(self, product_cost):
        assert self.is_element_present(*ProductPageLocators.ALERT_BASKET_COST), \
            "Сообщение о стоимости корзины не найдено"
        message = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_COST).text
        assert product_cost == message, f"В сообщении, о стоимости корзины, неверная сумма. Ожидаемая сумма {product_cost}, сообщение {message}"


