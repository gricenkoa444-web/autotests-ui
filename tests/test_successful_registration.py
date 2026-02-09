import pytest
from playwright.sync_api import Page, expect, Playwright
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.parametrize('email', ['test_email@gmail.com'])
@pytest.mark.parametrize('username', ['test_usename'])
@pytest.mark.parametrize('password', ['password'])

def test_successful_registration_one(registration_page: RegistrationPage, dashboard_page: DashboardPage,
                                 email: str, username: str, password: str):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_form(email=email, username=username, password=password)
    registration_page.click_registration_button()

    dashboard_page.check_title()