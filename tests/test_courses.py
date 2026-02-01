from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.focus()

        for char in 'test.user@gmail.com':
            page.keyboard.type(char, delay=300)

        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username_input.focus()

        for char in 'Test_username':
            page.keyboard.type(char, delay=300)

        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_password_input.focus()

        for char in 'TestPassword':
            page.keyboard.type(char, delay=300)

        registration_button_click = page.get_by_test_id('registration-page-registration-button')
        registration_button_click.click()

        context.storage_state(path='browser_one_test-state.json')

        page.wait_for_timeout(5000)