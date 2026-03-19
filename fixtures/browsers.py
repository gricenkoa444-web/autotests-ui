import pytest
from playwright.sync_api import sync_playwright, expect, Page, Playwright
import allure
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
from allure_commons.types import AttachmentType
from config import settings
from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(params=settings.browser)  # Добавляем параметризацию
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)


@pytest.fixture(scope='session')
def initialization_browse_state(playwright: Playwright):
        browser = playwright.chromium.launch(headless=settings.headless)
        context = browser.new_context()
        page = context.new_page()

        registration_page = RegistrationPage(page=page)
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill_form(
            email=settings.test_user_email, username=settings.test_user_username, password=settings.test_user_password
        )
        registration_page.click_registration_button()

        context.storage_state(path=settings.browser_state_file)
        browser.close()

@pytest.fixture(params=settings.browser)  # Добавляем параметризацию
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file
    )