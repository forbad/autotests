import allure
from tests.api.kabinet_agena import metods


@allure.title('Отправка заявки')
@allure.description('Отправка заявки с разрешенными символами')
@allure.severity(allure.severity_level.BLOCKER)
class TestSendOrders:
    def test_send_anket(self):
        metods.send_anket(metods.oauth_token_app())


