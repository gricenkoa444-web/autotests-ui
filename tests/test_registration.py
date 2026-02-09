#для того что бы запустить тестовый файл playwright_registration_one - его нужно обернуть в функцию
from playwright.sync_api import sync_playwright, Page
from pages.registration_page import RegistrationPage
import pytest

@pytest.mark.parametrize('email', ['test_email@gmail.com'])
@pytest.mark.parametrize('username', ['test_user_name'])
@pytest.mark.parametrize('password', ['password'])

def test_successful_registration(registration_page: RegistrationPage, email: str, username: str, password: str):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_form(email=email, username=username, password=password)
    registration_page.click_registration_button()





        #chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        #registration_email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        #registration_email_input.fill('user.name_test@gmail.com')

        #registration_username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        #registration_username_input.fill('Username')

        #registration_password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        #registration_password_input.fill('Password')

        #registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        #registration_button.click()

