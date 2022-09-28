import allure
from tests.api.kabinet_agena import metods


@allure.feature('Отправка заявки')
@allure.severity(allure.severity_level.BLOCKER)
class TestSendOrders:
    @allure.story('Отправка заявки с разрешенными символами')
    def test_send_anket(self):
        metods.send_anket(metods.oauth_token_app(), '\"Рога\" \'и\' «Копыта» - 0123456789', 201)

    @allure.story('Отправка заявки с запрещенными символамии')
    def test_send_anket_with_forbidden_characters(self):
        metods.send_anket(metods.oauth_token_app(), 'Hello world', 400)
