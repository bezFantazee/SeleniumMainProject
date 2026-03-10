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
        #time.sleep(200)
        self.should_be_massage_about_add_to_card()
        self.should_be_message_about_card_cost()

    def should_be_add_to_card_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CARD_BTN), \
            "Конпка добавления товара в корзину не найдена"

    def click_to_add_to_card_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BTN)
        button.click()

    def should_be_massage_about_add_to_card(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS), \
            "Сообщение об успешном добавлении товара не найдено"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Название товара не найдено"
        message = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS)
        product_name = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME)[-1]
        assert product_name.text in message.text, f"В сообщении, об успешном добавлении, не содержится имя товара. Имя товара {product_name}, Сообщение {message}"

    def should_be_message_about_card_cost(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_CARD_COST), \
            "Сообщение о стоимости корзины не найдено"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), \
            "Цена товара не найдена"
        message = self.browser.find_element(*ProductPageLocators.ALERT_CARD_COST)
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        assert product_cost.text in message.text, f"В сообщении, о стоимости корзины, неверная сумма. Ожидаемая сумма {product_cost}, сообщение {message}"


