import pytest

from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.fill_registration_form = RegistrationFormComponent(page)

        self.registration_button = page.get_by_test_id('registration-page-registration-button')

    def fill_form(self, email: str, username: str, password: str):
        self.fill_registration_form.fill_form(email, username, password)


    def click_registration_button(self):
        self.registration_button.click()


