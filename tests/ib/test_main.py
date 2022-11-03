import allure

@allure.title('Авторизация и разлогирование в браузерной версии ИБ')
def test_login_unlogin(desktop_app_auth):
    desktop_app_auth.test_cases.unauthorised_test()


@allure.title('Авторизация и разлогирование в мибильной версии ИБ')
def test_login_mobile(mobile_app_auth):
    mobile_app_auth.test_cases.unauthorised_test()
