#для того что бы запустить тестовый файл playwright_registration_one - его нужно обернуть в функцию
from pages.authentication.registration_page import RegistrationPage
import pytest
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @pytest.mark.parametrize('email', ['test_email@gmail.com'])
    @pytest.mark.parametrize('username', ['test_user_name'])
    @pytest.mark.parametrize('password', ['password'])
    @allure.title('Registration with correct  email, username and password')
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage, email: str, username: str, password: str):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill_form(email=email, username=username, password=password)
        registration_page.click_registration_button()



