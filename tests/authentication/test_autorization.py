import pytest
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.fill_registration_form.fill_form(email='Alisia@mail.ru', username='Alis', password='password')
        registration_page.click_registration_button()

        dashboard_page.dashboard_title.check_visible()
        dashboard_page.navbar.check_visible('Alis!')
        dashboard_page.sidebar_component.check_visible()
        dashboard_page.sidebar_component.click_logout()

        login_page.login_form.fill_form(email='Alisia@mail.ru', password='password')
        login_page.click_login_button()

        dashboard_page.dashboard_title.check_visible()
        dashboard_page.navbar.check_visible('Alis!')
        dashboard_page.sidebar_component.check_visible()




    @pytest.mark.parametrize('email', ['test.name@gmail.com'])
    @pytest.mark.parametrize('password', ['password_1'])
    def test_wrong_email_or_password(self, login_page: LoginPage, email: str, password: str):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.login_form.fill_form(email, password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    def test_navigation_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email='', username='', password='')



