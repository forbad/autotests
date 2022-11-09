import allure
from src.kabinet_agenta import metods


@allure.feature('Отправка заявки')
class TestSendOrders:
    @allure.title('Отправка заявки с разрешенными символами')
    def test_send_anket(self, api_request_context):
        metods.send_anket(api_request_context, metods.oauth_token_app(api_request_context), '\"Рога\" \'и\' «Копыта» - 0123456789', 201)

    @allure.title('Отправка заявки с запрещенными символамии')
    def test_send_anket_with_forbidden_characters(self, api_request_context):
        metods.send_anket(api_request_context, metods.oauth_token_app(api_request_context), 'Hello world', 400)
