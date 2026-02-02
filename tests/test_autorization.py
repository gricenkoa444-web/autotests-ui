from playwright.sync_api import sync_playwright, expect, Page

def test_wrong_email_or_password(chromium_page: Page):

        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        password_input = chromium_page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        password_input.fill('password')

        login_button = chromium_page.get_by_test_id("login-page-login-button")  # -указываем атрибут(более удобный)
        login_button.click()

        wrong_email_or_password_alert = chromium_page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

        chromium_page.wait_for_timeout(5000)