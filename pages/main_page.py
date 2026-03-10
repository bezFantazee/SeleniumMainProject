from selenium_main_project.SeleniumMainProject.pages.base_page import BasePage
from selenium_main_project.SeleniumMainProject.pages.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


