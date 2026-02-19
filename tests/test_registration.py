#для того что бы запустить тестовый файл playwright_registration_one - его нужно обернуть в функцию
from playwright.sync_api import sync_playwright, Page
from pages.registration_page import RegistrationPage
import pytest

@pytest.mark.parametrize('email', ['test_email@gmail.com'])
@pytest.mark.parametrize('username', ['test_user_name'])
@pytest.mark.parametrize('password', ['password'])

def test_successful_registration(registration_page: RegistrationPage, email: str, username: str, password: str):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form.fill_form(email=email, username=username, password=password)
    registration_page.click_registration_button()





