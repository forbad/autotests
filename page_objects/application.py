from playwright.sync_api import Playwright
from .test_cases import TestCases


class App:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url
        self.test_cases = TestCases(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def login(self, phone: str, password: str):
        self.page.locator("text=Вход").click()
        self.page.locator("input[name=\"phoneNumber\"]").fill(phone)
        self.page.locator("[aria-label=\"Modal\"] >> text=Далее").click()
        self.page.locator("input[name=\"password\"]").click()
        self.page.locator("input[name=\"password\"]").fill(password)
        self.page.locator("text=Войти").click()
        self.page.wait_for_url("https://test-ib.mybank.by/main_unauthorised")

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

