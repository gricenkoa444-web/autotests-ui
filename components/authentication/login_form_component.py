from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text
from elements.input import Input

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'authentication-ui-course-title-text', 'UI Course - title')
        self.login = Input(page, 'login-form-email-input', 'Email')
        self.password = Input(page, 'login-form-password-input', 'Password')


    def fill_form(self, email, password):
        self.login.fill(email)
        self.password.fill(password)

    def check_visible(self, email, password):
        self.title.check_visible()
        self.title.check_have_text('UI Course')

        self.login.check_visible()
        self.login.check_have_text(email)

        self.password.check_visible()
        self.password.check_have_text(password)