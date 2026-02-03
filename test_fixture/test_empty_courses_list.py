import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_empty_courses_list_1(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    title_text_courses = chromium_page_with_state.get_by_test_id('courses-drawer-list-item-title-text')
    expect(title_text_courses).to_be_visible()
    expect(title_text_courses).to_have_text('Courses')

    button_courses_click = chromium_page_with_state.get_by_test_id('courses-drawer-list-item-button')
    button_courses_click.click()

    toolbar_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(toolbar_text).to_be_visible()
    expect(toolbar_text).to_have_text('Courses')

    title_empty_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(title_empty_block).to_be_visible()
    expect(title_empty_block).to_have_text('There is no results')

    text_empty_results = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(text_empty_results).to_be_visible()
    expect(text_empty_results).to_have_text('Results from the load test pipeline will be displayed here')


    chromium_page_with_state.wait_for_timeout(5000)