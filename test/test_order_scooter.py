import allure
from urls import Url
from pages.order_scooter_page import OrderPage
from locators.locators_home_page import  LocatorsHomePage
from locators.locators_order_scooter_page import LocatorsOrderingScooter
from data import UserData

class TestOrderScooter:

    @allure.title('Возможность сделать заказ через кнопку "Заказать" в шапке сайта')
    def test_order_button_in_header(self, driver):
        page = OrderPage(driver)
        page.open_order_form(LocatorsHomePage.ORDER_BUTTON_CAP)
        user_data = UserData.USER_2
        page.filling_form_whom_the_scooter(user_data=user_data)
        page.filling_form_about_rent(comment_for_courier=user_data["comment_for_courier"])
        page.click_on_element(LocatorsOrderingScooter.BUTTON_YES)
        page.wait_for_text_to_be_present(
            LocatorsOrderingScooter.WINDOW_ORDER_PLACED,
            UserData.ORDER_CONFIRMATION_WINDOW
        )
        current_text = driver.find_element(*LocatorsOrderingScooter.WINDOW_ORDER_PLACED).text
        expected_text = UserData.ORDER_CONFIRMATION_WINDOW
        assert expected_text in current_text

    @allure.title('Возможность сделать заказ через кнопку "Заказать" в блоке "Как это работает"')
    def test_order_button_in_how_this_work(self, driver):
        page = OrderPage(driver)
        page.open_site()
        user_data = UserData.USER_1
        page.scroll_to_and_click_element(LocatorsHomePage.ORDER_BUTTON_HOW_IT_WORKS)
        page.filling_form_whom_the_scooter(user_data=user_data)
        page.filling_form_about_rent(comment_for_courier=user_data["comment_for_courier"])
        page.click_on_element(LocatorsOrderingScooter.BUTTON_YES)
        page.wait_for_text_to_be_present(
            LocatorsOrderingScooter.WINDOW_ORDER_PLACED,
            UserData.ORDER_CONFIRMATION_WINDOW
        )
        current_text = driver.find_element(*LocatorsOrderingScooter.WINDOW_ORDER_PLACED).text
        expected_text = UserData.ORDER_CONFIRMATION_WINDOW
        assert expected_text in current_text

    @allure.title('Переход на главную страницу "Самокат" при клике на логотип "Самоката" после успешного заказа')
    def test_click_logo_home_page(self, driver):
        page = OrderPage(driver)
        page.open_order_form(LocatorsHomePage.ORDER_BUTTON_CAP)
        user_data = UserData.USER_1
        page.filling_form_whom_the_scooter(user_data=user_data)
        page.filling_form_about_rent(comment_for_courier=user_data["comment_for_courier"])
        page.click_on_element(LocatorsOrderingScooter.BUTTON_YES)
        page.click_on_element(LocatorsOrderingScooter.BUTTON_VIEW_STATUS)
        page.click_on_element(LocatorsOrderingScooter.SCOOTER_LOGO)
        page.wait_for_url_to_be(Url.HOME_PAGE)
        current_url = driver.current_url
        expected_url = Url.HOME_PAGE
        assert current_url == expected_url

    @allure.title('Переход на главную страницу "Дзена" при клике на логотип "Яндекс" после успешного заказа')
    def test_click_yandex_open_dzen(self, driver):
        page = OrderPage(driver)
        page.open_order_form(LocatorsHomePage.ORDER_BUTTON_CAP)
        user_data = UserData.USER_1
        page.filling_form_whom_the_scooter(user_data=user_data)
        page.filling_form_about_rent(comment_for_courier=user_data["comment_for_courier"])
        page.click_on_element(LocatorsOrderingScooter.BUTTON_YES)
        page.click_on_element(LocatorsOrderingScooter.BUTTON_VIEW_STATUS)
        page.click_on_element(LocatorsOrderingScooter.YANDEX_LOGO)
        new_window_url = page.switch_to_new_window_and_wait_for_url(Url.DZEN_PAGE)
        current_url = new_window_url
        expected_url = Url.DZEN_PAGE
        assert current_url == expected_url