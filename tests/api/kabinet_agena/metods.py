import json

import allure
import requests
from src.variables.kabinet_agenta import data_ka


def oauth_token_app():
    """
    Получение токена от имени клиента
    :return: accessToken от имени клиента
    """
    url = data_ka.url_stend + data_ka.url_api_login

    payload = json.dumps({
        "email": data_ka.user[0],
        "password": data_ka.user[1]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['accessToken']


def send_anket(oauth_token_app):
    """
    Проверяем успешную отправку заявки
    :param oauth_token_app: Токен для отправки запроса от имени пользователя
    """
    url = data_ka.url_stend + data_ka.url_api_orders

    payload = json.dumps({
        "city": data_ka.anketa['city'],
        "fullName": data_ka.anketa['fullName'],
        "organizationName": data_ka.anketa['organizationName'],
        "phoneNumber": data_ka.anketa['phoneNumber'],
        "productCode": data_ka.anketa['productCode'],
        "unp": data_ka.anketa['unp']
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {oauth_token_app}'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 201, f'Запрос для получения токена фин. приложения вернул статус {response.status_code}.'