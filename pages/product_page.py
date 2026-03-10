import time
from urllib.parse import parse_qs, urlparse

from selenium.webdriver.common.by import By

from selenium_main_project.SeleniumMainProject.pages.base_page import BasePage
from selenium_main_project.SeleniumMainProject.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_card(self):
        self.should_be_add_to_card_button()
        self.click_to_add_to_card_button()
        self.solve_quiz_and_get_code()#вычисление математического выражения
        self.should_be_massage_about_add_to_card(self.get_product_name())
        self.should_be_message_about_card_cost(self.get_product_cost())

    def should_be_add_to_card_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CARD_BTN), \
            "Конпка добавления товара в корзину не найдена"

    def click_to_add_to_card_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BTN)
        button.click()

    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.H1), \
            "Название товара не найдено"
        return self.browser.find_elements(*ProductPageLocators.H1)[-1].text

    def get_product_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), \
            "Цена товара не найдена"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text

    def should_be_massage_about_add_to_card(self, product_name):
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS), \
            "Сообщение об успешном добавлении товара не найдено"

        message = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS).text
        assert product_name == message, f"В сообщении, об успешном добавлении, не содержится имя товара. Имя товара {product_name}, Сообщение {message}"

    def should_be_message_about_card_cost(self, product_cost):
        assert self.is_element_present(*ProductPageLocators.ALERT_CARD_COST), \
            "Сообщение о стоимости корзины не найдено"
        message = self.browser.find_element(*ProductPageLocators.ALERT_CARD_COST).text
        assert product_cost == message, f"В сообщении, о стоимости корзины, неверная сумма. Ожидаемая сумма {product_cost}, сообщение {message}"


