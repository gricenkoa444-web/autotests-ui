import pytest
from pages.authentication.registration_page import RegistrationPage
import allure

@pytest.mark.parametrize('email', ['test_email@gmail.com'])
@pytest.mark.parametrize('username', ['test_usename'])
@pytest.mark.parametrize('password', ['password'])
@allure.title('Duble registration with correct email, username and password')
def test_successful_registration_one(registration_page: RegistrationPage, email: str, username: str, password: str):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill_form(email=email, username=username, password=password)
    registration_page.click_registration_button()





