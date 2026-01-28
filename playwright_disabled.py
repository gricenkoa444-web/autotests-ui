from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
#Проверяем что кнопка to_be_disabled
    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_disabled()

    #page.wait_for_timeout(5000)
#Проверяем, что кнопка not_to_be_disabled
    login_email_input = page.get_by_test_id("login-form-email-input").locator('input')
    login_email_input.fill('12345')

    login_password_input = page.get_by_test_id('login-form-password-input').locator('input')
    login_password_input.fill('password')

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).not_to_be_disabled()
