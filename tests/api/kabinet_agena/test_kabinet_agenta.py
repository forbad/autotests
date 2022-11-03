import allure
from src.variables.kabinet_agenta import metods


@allure.feature('Отправка заявки')
class TestSendOrders:
    @allure.title('Отправка заявки с разрешенными символами')
    def test_send_anket(self):
        metods.send_anket(metods.oauth_token_app(), '\"Рога\" \'и\' «Копыта» - 0123456789', 201)

    @allure.title('Отправка заявки с запрещенными символамии')
    def test_send_anket_with_forbidden_characters(self):
        metods.send_anket(metods.oauth_token_app(), 'Hello world', 400)
