import allure
from src.kabinet_agenta import data_ka


@allure.step
def oauth_token_app(api_request_context):
    """
    Получение токена от имени клиента
    :param api_request_context: fixure in file confest.py
    :return: accessToken от имени клиента
    """

    data = {
        "email": data_ka.user[0],
        "password": data_ka.user[1]

    }
    response = api_request_context.post(
        data_ka.url_api_login, data=data
    )
    assert response.ok
    return response.json()['accessToken']


@allure.step
def send_anket(api_request_context, token, organization_name, expected_result) -> None:
    """
    Проверяем успешную отправку заявки
    :param expected_result: expected_result
    :param organization_name: organization_name
    :param api_request_context: fixure in file confest.py
    :param token: Токен для отправки запроса от имени пользователя
    """

    data = {
        "city": data_ka.anketa['city'],
        "fullName": data_ka.anketa['fullName'],
        "organizationName": organization_name,
        "phoneNumber": data_ka.anketa['phoneNumber'],
        "productCode": data_ka.anketa['productCode'],
        "unp": data_ka.anketa['unp']
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    response = api_request_context.post(
        data_ka.url_api_orders, headers=headers, data=data
    )
    assert response.status == expected_result, f'Запрос для получения токена фин. приложения вернул статус {response.status}.'
