import pytest
from playwright.sync_api import sync_playwright, expect, Page, Playwright

@pytest.fixture
def chromium_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture(scope='session')
def initialization_browse_state(playwright: Playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill('test.use@gmail.com')

        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username_input.fill('test_username')

        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_password_input.fill('password')

        registration_button_click = page.get_by_test_id('registration-page-registration-button')
        registration_button_click.click()

        context.storage_state(path='browser-state.json')
        browser.close()

@pytest.fixture(scope='function')
def chromium_page_with_state(initialization_browse_state, playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page =  context.new_page()
        yield page
        browser.close()
