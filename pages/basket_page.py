from selenium_main_project.SeleniumMainProject.pages.base_page import BasePage
from selenium_main_project.SeleniumMainProject.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Товары в корзине были найдены, но должны отсутствовать"

    def should_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Сообщение о пустой корзине не найдено"
