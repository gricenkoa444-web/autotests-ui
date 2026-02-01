from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.ui
class TestMarkHomework:
    @pytest.mark.smoke
    def test_open_sites_smoke(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

            print('1.Test_open_sites_smoke is ok')

    @pytest.mark.smoke
    @pytest.mark.critical
    @pytest.mark.regression
    def test_login(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

            login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
            login_email_input.fill('user.name@gmail.com')

            login_password_input = page.get_by_test_id('login-form-password-input').locator('input')
            login_password_input.fill('password')

            login_button_click = page.get_by_test_id('login-page-login-button')
            login_button_click.click()

            print('2.Test_login is ok')

    @pytest.mark.regression
    def test_registration_save_json(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = browser.new_page()

            page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

            registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
            registration_email_input.fill('test.username@gmail.com')

            registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
            registration_username_input.fill('test_username')

            registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
            registration_password_input.fill('password')

            registration_button_click = page.get_by_test_id('registration-page-registration-button')
            registration_button_click.click()

            context.storage_state(path='test_new_browser.json')

            print('3.Test_registration_save_json is ok')
    @pytest.mark.smoke
    def test_open_dashboard(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context(storage_state='browser_one_test-state.json')
            page = context.new_page()

            page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/dashboard')

            title_text_visible = page.get_by_test_id('navigation-navbar-app-title-text')
            expect(title_text_visible).to_be_visible()
            expect(title_text_visible).to_have_text('UI Course')

            icon_dashboard = page.get_by_test_id('dashboard-drawer-list-item-icon')
            expect(icon_dashboard).to_be_visible()

            text_dashboard = page.get_by_test_id('dashboard-drawer-list-item-title-text')
            expect(text_dashboard).to_have_text('Dashboard')

            icon_courses = page.get_by_test_id('courses-drawer-list-item-icon')
            expect(icon_courses).to_be_visible()

            test_courses = page.get_by_test_id('courses-drawer-list-item-title-text')
            expect(test_courses).to_have_text('Courses')

            button_logout = page.get_by_test_id('logout-drawer-list-item-button')
            expect(button_logout).to_be_visible()

            icon_logout = page.get_by_test_id('logout-drawer-list-item-icon')
            expect(icon_logout).to_be_visible()

            text_logout = page.get_by_test_id('logout-drawer-list-item-title-text')
            expect(text_logout).to_have_text('Logout')

            print('4.Test_open_dashboard is ok')

