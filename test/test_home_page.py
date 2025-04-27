import allure
import pytest
from pages.home_page import HomePage
from data import QuestionAnswers
from locators.locators_home_page import LocatorsHomePage


@pytest.mark.parametrize(
        "locator_question, locator_answer, answer_text",
        [
            (LocatorsHomePage.HOW_IT_COST, LocatorsHomePage.HOW_IT_COST_TEXT, QuestionAnswers.RENTAL_PRICE),
            (LocatorsHomePage.SEVERAL_SCOOTER, LocatorsHomePage.SEVERAL_SCOOTER_TEXT, QuestionAnswers.MULTIPLE_SCOOTERS),
            (LocatorsHomePage.RENTAL_TIME_CALCULATION, LocatorsHomePage.RENTAL_TIME_CALCULATION_TEXT, QuestionAnswers.RENTAL_DURATION),
            (LocatorsHomePage.ORDER_SCOOTER_TODAY, LocatorsHomePage.ORDER_SCOOTER_TODAY_TEXT, QuestionAnswers.ORDER_SCOOTER_NOW),
            (LocatorsHomePage.EXTEND_OR_RETURN_SCOOTER, LocatorsHomePage.EXTEND_OR_RETURN_SCOOTER_TEXT, QuestionAnswers.EXTEND_OR_RETURN_POLICY),
            (LocatorsHomePage.CHARGING_SCOOTER, LocatorsHomePage.CHARGING_SCOOTER_TEXT, QuestionAnswers.SCOOTER_CHARGING),
            (LocatorsHomePage.CANCEL_ORDER, LocatorsHomePage.CANCEL_ORDER_TEXT, QuestionAnswers.ORDER_CANCELLATION),
            (LocatorsHomePage.OUTSIDE_MKAD, LocatorsHomePage.OUTSIDE_MKAD_TEXT, QuestionAnswers.DELIVERY_OUTSIDE_CITY)
        ]
    )

@allure.title("При нажатии на стрелочку выпадающего списка в разделе «Вопросы о важном» открывается соответствующий текст")
def test_faq_questions(driver, locator_question, locator_answer, answer_text):
    page = HomePage(driver)
    page.open_site()
    page.scroll_to_and_click_element(locator_question)
    real_text = page.get_text_from_element(locator_answer)
    expect_text = answer_text
    assert real_text == expect_text