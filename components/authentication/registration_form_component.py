from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('authentication-ui-course-title-text')

        self.email = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password = page.get_by_test_id('registration-form-password-input').locator('input')

    def fill_form(self, email:str, username:str, password:str):
        expect(self.email).to_be_visible()
        self.email.fill(email)

        expect(self.username).to_be_visible()
        self.username.fill(username)

        expect(self.password).to_be_visible()
        self.password.fill(password)

    def check_visible(self, email:str, username:str, password:str):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('UI Course')

        expect(self.email).to_be_visible()
        expect(self.email).to_have_text(email)

        expect(self.username).to_be_visible()
        expect(self.username).to_have_text(username)

        expect(self.password).to_be_visible()
        expect(self.password).to_have_text(password)






