import allure
from playwright.sync_api import Page


class TestCases:
    def __init__(self, page: Page):
        self.page = page


    @allure.step
    def unauthorised_test(self):
        self.page.locator(".user-short-name").click()
        self.page.locator("text=Выйти").click()
        self.page.wait_for_url("https://test-ib.mybank.by/main_unauthorised")
