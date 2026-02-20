from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from elements.text import Text
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'authentication-ui-course-title-text', 'UI Course Title')

        self.email = Input(page, 'registration-form-email-input', 'Email Input')
        self.username = Input(page, 'registration-form-username-input', 'Username Input')
        self.password = Input(page, 'registration-form-password-input', 'Password Input')

        self.dashboard_toolbar = DashboardToolbarViewComponent(page)

    def fill_form(self, email:str, username:str, password:str):
        self.email.fill(email)
        self.email.check_have_value(email)

        self.username.fill(username)
        self.username.check_have_value(username)

        self.password.fill(password)
        self.password.check_have_value(password)

    def check_visible(self, email:str, username:str, password:str):
        self.title.check_visible()
        self.title.check_have_text('UI Course')

        self.email.check_visible()
        self.email.check_have_value(email)

        self.username.check_visible()
        self.username.check_have_value(username)

        self.password.check_visible()
        self.password.check_have_value(password)






