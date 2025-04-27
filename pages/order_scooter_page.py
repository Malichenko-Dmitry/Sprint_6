import allure
from locators.locators_order_scooter_page import LocatorsOrderingScooter
from pages.home_page import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(HomePage):

    @allure.step('Открытие формы заказа')
    def open_order_form(self, locator):
        self.open_site()
        self.click_on_element(locator)

    @allure.step('Клик по полю и ввод значения')
    def fill_in_field(self, locator, data):
        self.click_on_element(locator)
        self.set_text_to_element(locator,data)

    @allure.step('Заполнение формы заказа на странице "Для кого самокат"')
    def filling_form_whom_the_scooter(self, user_data=None):
        self.fill_in_field(LocatorsOrderingScooter.FIELD_NAME, user_data["name"])
        self.fill_in_field(LocatorsOrderingScooter.FIELD_SURNAME, user_data["surname"])
        self.fill_in_field(LocatorsOrderingScooter.FIELD_ADDRESS, user_data["address"])
        self.click_on_element(LocatorsOrderingScooter.FIELD_METRO)
        self.click_on_element(LocatorsOrderingScooter.KALUZHSKAYA)
        self.fill_in_field(LocatorsOrderingScooter.FIELD_PHONE, user_data["phone"])
        self.click_on_element(LocatorsOrderingScooter.BUTTON_NEXT)

    @allure.step('Заполнение формы заказа на странице "Про аренду"')
    def filling_form_about_rent(self, comment_for_courier):
        self.click_on_element(LocatorsOrderingScooter.FIELD_RENTAL_START)
        self.click_on_element(LocatorsOrderingScooter.RENTAL_START_DATE)
        self.click_on_element(LocatorsOrderingScooter.FIELD_RENTAL_PERIOD)
        self.click_on_element(LocatorsOrderingScooter.TWO_DAYS)
        self.click_on_element(LocatorsOrderingScooter.FIELD_SCOOTER_COLOR)
        self.fill_in_field(LocatorsOrderingScooter.FIELD_COMMENT_FOR_COURIER, comment_for_courier)
        self.click_on_element(LocatorsOrderingScooter.ORDER_BUTTON)

    @allure.step('Ожидание появления текста в элементе')
    def wait_for_text_to_be_present(self, locator, text, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    @allure.step('Ожидание URL страницы')
    def wait_for_url_to_be(self, url, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключение на новое окно и ожидание URL')
    def switch_to_new_window_and_wait_for_url(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)
        new_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window_handle)

        self.wait_for_url_to_be(expected_url)
        return self.get_current_url()