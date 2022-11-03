import logging
import allure
from playwright.sync_api import Browser
from playwright.sync_api import ConsoleMessage, Dialog
from page_objects.test_cases import TestCases


class App:
    def __init__(self, browser: Browser, base_url: str, **kwargs):
        self.browser = browser
        self.context = self.browser.new_context(**kwargs)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.test_cases = TestCases(self.page)

        def console_handler(message: ConsoleMessage):
            if message.type == 'error':
                logging.error(f'page: {self.page.url}, console error: {message.text}')

        def dialog_handler(dialog: Dialog):
            logging.warning(f'page: {self.page.url}, dialog text: {dialog.message}')
            dialog.accept()

        self.page.on('console', console_handler)
        self.page.on('dialog', dialog_handler)

    @allure.step
    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    @allure.step
    def login(self, phone: str, password: str):
        self.page.locator("text=Вход").click()
        self.page.locator("input[name=\"phoneNumber\"]").fill(phone)
        self.page.locator("[aria-label=\"Modal\"] >> text=Далее").click()
        self.page.locator("input[name=\"password\"]").click()
        self.page.locator("input[name=\"password\"]").fill(password)
        self.page.locator("text=Войти").click()
        self.page.wait_for_url("https://test-ib.mybank.by/main_unauthorised")

    @allure.step
    def close(self):
        self.page.close()
        self.context.close()
