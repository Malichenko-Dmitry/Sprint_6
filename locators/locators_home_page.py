from selenium.webdriver.common.by import By

class LocatorsHomePage:

    CLOSE_COOKIES = By.ID, "rcc-confirm-button"
    # Кнопка, закрывающая куки. "да все привыкли"

    HOW_IT_COST = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'Сколько это стоит?')]"
    # Выпадающий список. "Сколько это стоит? И как оплатить?"

    HOW_IT_COST_TEXT = By.XPATH, "//p[contains(text(), 'Сутки — 400 рублей.')]"
    # Выпадающий список. Ответ выпадающего списка "Сколько это стоит? И как оплатить?"

    SEVERAL_SCOOTER = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'Хочу сразу несколько самокатов!')]"
    # Выпадающий список.  "Хочу сразу несколько самокатов! Так можно?"

    SEVERAL_SCOOTER_TEXT = By.XPATH, "//p[contains(text(), 'Пока что у нас так: один заказ — один самокат.')]"
    # Выпадающий список. Ответ выпадающего списка "Хочу сразу несколько самокатов! Так можно?"

    RENTAL_TIME_CALCULATION = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'Как рассчитывается время')]"
    # Выпадающий список. "Как рассчитывается время аренды?"

    RENTAL_TIME_CALCULATION_TEXT = By.XPATH, "//p[contains(text(), 'Допустим, вы оформляете заказ')]"
    # Выпадающий список. Ответ выпадающего списка "Как рассчитывается время аренды?"

    ORDER_SCOOTER_TODAY = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'Можно ли заказать самокат')]"
    # Выпадающий список. "Можно ли заказать самокат прямо на сегодня?"

    ORDER_SCOOTER_TODAY_TEXT = By.XPATH, "//p[contains(text(), 'Только начиная с завтрашнего дня.')]"
    # Выпадающий список. Ответ выпадающего списка "Можно ли заказать самокат прямо на сегодня?"

    EXTEND_OR_RETURN_SCOOTER = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'продлить заказ или вернуть самокат раньше')]"
    # Выпадающий список. "Можно ли продлить заказ или вернуть самокат раньше?"

    EXTEND_OR_RETURN_SCOOTER_TEXT = By.XPATH, "//p[contains(text(), 'Пока что нет!')]"
    # Выпадающий список. Ответ выпадающего списка "Можно ли заказать самокат прямо на сегодня?"

    CHARGING_SCOOTER =  By.XPATH, "//div[@class='accordion__button' and contains(text(), 'зарядку вместе с самокатом')]"
    # Выпадающий список. "Вы привозите зарядку вместе с самокатом?"

    CHARGING_SCOOTER_TEXT = By.XPATH, "//p[contains(text(), 'приезжает к вам с полной зарядкой')]"
    # Выпадающий список. Ответ выпадающего списка "Можно ли заказать самокат прямо на сегодня?"

    CANCEL_ORDER = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'отменить заказ')]"
    # Выпадающий список. "Можно ли отменить заказ?"

    CANCEL_ORDER_TEXT = By.XPATH, "//p[contains(text(), 'Да, пока самокат не привезли.')]"
    # Выпадающий список. Ответ выпадающего списка "Можно ли отменить заказ?"

    OUTSIDE_MKAD = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'МКАДом, привезёте?')]"
    # Выпадающий список. "Я жизу за МКАДом, привезёте?"

    OUTSIDE_MKAD_TEXT = By.XPATH, "//p[contains(text(), 'И Москве, и Московской области.')]"
    # Выпадающий список. Ответ выпадающего списка "Я жизу за МКАДом, привезёте?"

    ORDER_BUTTON_CAP = By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']"
    # Домашняя страница. Шапка сайта. Кнопка "Заказать"

    ORDER_BUTTON_HOW_IT_WORKS = By.CSS_SELECTOR, ".Home_FinishButton__1_cWm > button.Button_Button__ra12g"
    # Домашняя страница. Блок "Как это работает". Кнопка "Заказать"