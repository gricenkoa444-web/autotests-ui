from playwright.sync_api import sync_playwright, Page
import pytest

@pytest.mark.parametrize('email', ['test.name@gmail.com', 'user.name@gmail.com', 'empty.name@gmail.com'])
@pytest.mark.parametrize('password', ['password_1', 'password_2', 'password_3'])
def test_registration_06(chromium_page: Page, email: str, password: str):


            chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

            registration_email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
            registration_email_input.fill('')

            registration_username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
            registration_username_input.fill('Username')

            registration_password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
            registration_password_input.fill('')

            registration_button_click = chromium_page.get_by_test_id('registration-page-registration-button')
            registration_button_click.click







