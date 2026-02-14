from playwright.sync_api import sync_playwright, expect
import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize('email', ['test.name@gmail.com', 'user.name@gmail.com', 'empty.name@gmail.com'])
@pytest.mark.parametrize('password', ['password_1', 'password_2', 'password_3'])
def test_wrong_email_or_password(login_page: LoginPage, email: str, password: str):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.fill_login_form(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()


# До использования POM
        #chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        #email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        #email_input.fill(email)


        #password_input = chromium_page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        #password_input.fill(password)

        #login_button = chromium_page.get_by_test_id("login-page-login-button")  # -указываем атрибут(более удобный)
        #login_button.click()

        #wrong_email_or_password_alert = chromium_page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
        #expect(wrong_email_or_password_alert).to_be_visible()
        #expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

        #chromium_page.wait_for_timeout(5000)