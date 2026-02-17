from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('authentication-ui-course-title-text')
        self.login = page.get_by_test_id('login-form-email-input').locator('input')
        self.password = page.get_by_test_id('login-form-password-input').locator('input')

    def fill_form(self, email: str, password: str):
        self.login.fill(email)

        self.password.fill(password)

    def check_visible(self, email: str, password: str):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('UI Course')

        expect(self.login).to_be_visible()
        expect(self.login).to_have_text(email)

        expect(self.password).to_be_visible()
        expect(self.password).to_have_text(password)