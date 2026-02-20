import pytest

from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from elements.button import Button


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.fill_registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page, 'registration-page-registration-button', 'Button')

    def fill_form(self, email: str, username: str, password: str):
        self.fill_registration_form.fill_form(email, username, password)


    def click_registration_button(self):
        self.registration_button.click()


