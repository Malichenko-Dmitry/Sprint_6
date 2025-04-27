import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Url
from locators.locators_home_page import LocatorsHomePage

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step('Открытие главной страницы сайта')
    def open_site(self):
        self.driver.get(Url.HOME_PAGE)

    @allure.step('Закрытие окна с куками')
    def close_cookies(self):
        cookie_close_button = self.wait.until(
            EC.element_to_be_clickable(LocatorsHomePage.CLOSE_COOKIES)
        )
        cookie_close_button.click()

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Прокрутка до элемента и клик по нему')
    def scroll_to_and_click_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait.until(EC.visibility_of(element))
        element.click()
        return element

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('Ввод текста в элемент')
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)