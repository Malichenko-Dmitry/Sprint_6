from selenium.webdriver.common.by import By

class LocatorsOrderingScooter:

    FIELD_NAME = By.XPATH, "//input[contains(@class, 'Input_Responsible') and @placeholder='* Имя']"
    # Страница "Для кого самокат". Поле "Имя"

    FIELD_SURNAME = By.XPATH, "//input[contains(@class, 'Input_Responsible') and @placeholder='* Фамилия']"
    # Страница "Для кого самокат". Поле "Фамилия"

    FIELD_ADDRESS = By.XPATH, "//input[contains(@class, 'Input_Responsible') and @placeholder='* Адрес: куда привезти заказ']"
    # Страница "Для кого самокат". Поле "Адрес"

    FIELD_METRO = By.XPATH, "//input[@placeholder='* Станция метро']"
    # Страница "Для кого самокат". Поле "Метро"

    KALUZHSKAYA = By.XPATH, "//div[@class='Order_Text__2broi' and text()='Калужская']"
    # Страница "Для кого самокат". Поле "Метро" Станция "Калужская"

    FIELD_PHONE = By.XPATH, "//input[contains(@class, 'Input_Responsible') and @placeholder='* Телефон: на него позвонит курьер']"
    # Страница "Для кого самокат". Поле "Телефон"

    BUTTON_NEXT = By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Далее']"
    # Страница "Для кого самокат". Кнопка "Далее"

    FIELD_RENTAL_START = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    # Страница "Про аренду". Поле "Когда привезти самокат"

    RENTAL_START_DATE = By.XPATH, "//div[contains(@aria-label, '30-е апреля') and text()='30']"
    # Страница "Про аренду". Календарь

    FIELD_RENTAL_PERIOD = By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and text()='* Срок аренды']"
    # Страница "Про аренду". Поле "Срок аренды"

    TWO_DAYS = By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']"
    # Страница "Про аренду". Выпадающий список "Срок аренды". "Двое суток"

    FIELD_SCOOTER_COLOR = By.XPATH, "//input[@id='black' and @type='checkbox']"
    # Страница "Про аренду". Поле "Цвет самоката". "чёрный жемчуг"

    FIELD_COMMENT_FOR_COURIER = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    # Страница "Про аренду". Поле "Комментарий для курьера"

    ORDER_BUTTON = By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']"
    # Страница "Про аренду". Кнопка "Заказать"

    BUTTON_YES = By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Да']"
    # Страница "Про аренду". Окно "Хотите оформить заказ?". Кнопка "Да"

    WINDOW_ORDER_PLACED = By.XPATH, "//div[contains(@class, 'ModalHeader') and contains(., 'Заказ оформлен')]"
    # Страница "Про аренду". Окно "Заказ оформлен"

    BUTTON_VIEW_STATUS = By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Посмотреть статус']"
    # Страница "Про аренду". Окно "Заказ оформлен"ю Кнопка "Посмотреть статус"

    SCOOTER_LOGO = By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR"
    # Страница "Статус заказа". Логотип "Самокат"

    YANDEX_LOGO = By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI"
    # Страница "Статус заказа". Логотип "Яндекс"