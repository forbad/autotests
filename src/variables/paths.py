class Paths:

    # Unauthorised-LoginForm
    TITLE_UNAUTHORISED = 'Главная неавторизованная'
    ENTER_BUTTON = '//span[text()="Вход"]'
    NEXT_BUTTON = '//form[@class="login-form"]//button[contains(text(),"Далее")]'
    COME_IN_BUTTON = '//button[text()="Войти"]'
    PHONE_INPUT = '//input[@name="phoneNumber"]'
    PASSWORD_INPUT = '//input[@name = "password"]'
    FORGOT_PASSWORD = '//span[text()="Забыли пароль?"]'
    SMS_INPUT = '//label[contains(text(), "Код из СМС")]/following::input[1]'
    ID_INPUT = '//input[@name = "personalNumber"]'
    NEW_PASSWORD = '// input[ @ name = "newPassword"]'
    NEW_PASSWORD_CONFIRMATION = '// input[ @ name = "newPassword2"]'
    SAVE_AND_ENTER_BUTTON = '//button[text()="Сохранить и войти"]'

    # Unauthorised-p2p-transfer
    P2P_WIDGET = '//div[contains(@class,"widget-money-transfer-wrap")]'
    SENDER_CARD_NUMBER_COMBO_BOX = '//div[contains(@name,"senderCardNumberSelected")]'
    SENDER_CARD_NUMBER = '//input[contains(@name,"senderCardNumber")]'
    MOUNT = '//div[text()="Месяц"]'
    YEAR = '//div[text()="Год"]'
    NEXT_BTN = '//*[contains(text(),"Далее")]'
    CVV = '//input[contains(@name,"cvv")]'
    RECIPIENT_CARD_NUMBER_COMBO_BOX = '//div[contains(@name,"recipientCardNumberSelected")]'
    RECIPIENT_CARD_NUMBER = '//input[contains(@name,"recipientCardNumber")]'
    SUM = '//input[contains(@name,"sum")]'
    OPERATION_CONFIRMATION = '//font[text()="Подтверждение операции"]'
    AGREE_CHECK_BOX = '//input[@name="agree"]/..//*[name()="svg" and position()=1]'
    SMS = '//input[contains(@name,"smsCode")]'
    TRANSFER = '//button[text()="Перевести"]'
    WIDGET_TITLE = '//div[contains(@class,"widget-money-transfer")]//div[@class="widget-title-block"]'
    RECIPIENT_NAME = '//input[contains(@name,"recipientName")]'
    SURNAME = '//input[contains(@name,"recipientSurname")]'
    COMMISSION = '//span[@name="commission"]'

    # Authorised
    SHORT_NAME_BUTTON = '//span[@class="user-short-name"]'
    EXIT_BUTTON = '//div[@class="header-role exit"]/span[text()="Выйти"]'
