import allure
from playwright.sync_api import Page, expect
from src.variables.paths import Paths as p
from src.variables.data import Data as d


@allure.title('Авторизция')
@allure.description('Авторизция клиента без SMS-подтверждения')
@allure.severity(allure.severity_level.BLOCKER)
def test_run(page: Page):
    # Go to https://test-ib.mybank.by:8086/main_unauthorised
    page.goto(d.URL_ADDRESS)
    # Click header >> text=Вход
    page.locator("header >> text=Вход").click()
    # Fill input[name="phoneNumber"]
    page.locator("input[name=\"phoneNumber\"]").fill("(29)761-21-14_")
    # Click [aria-label="Modal"] >> text=Далее
    page.locator("[aria-label=\"Modal\"] >> text=Далее").click()
    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("Qq111111")
    # Click text=Войти
    page.locator("text=Войти").click()
    page.wait_for_url("https://test-ib.mybank.by:8086/main_authorised")
    # Click button:has-text("СГ")
    page.locator(p.SHORT_NAME_BUTTON).click()
    # Click text=Выйти
    page.locator("text=Выйти").click()
    assert page.locator("text=Выйти").is_visible()
    page.wait_for_url("https://test-ib.mybank.by:8086/main_unauthorised")

