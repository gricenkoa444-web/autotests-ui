import pytest
from playwright.sync_api import sync_playwright, expect, Page
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list_1(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_list_page.navbar.check_visible(' test_username!')
    courses_list_page.sidebar_component.check_visible()
    courses_list_page.check_visible_courses_title()
    courses_list_page.chek_visible_create_course_button()
    courses_list_page.check_visible_empty_view()
    courses_list_page.click_create_course_button()
    create_course_page.check_visible_create_course_title()
    create_course_page.check_visible_create_course_button()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()









    #button_courses_click = chromium_page_with_state.get_by_test_id('courses-drawer-list-item-button')
    #button_courses_click.click()

    #toolbar_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    #expect(toolbar_text).to_be_visible()
    #expect(toolbar_text).to_have_text('Courses')

    #title_empty_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    #expect(title_empty_block).to_be_visible()
    #expect(title_empty_block).to_have_text('There is no results')

    #text_empty_results = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    #expect(text_empty_results).to_be_visible()
    #expect(text_empty_results).to_have_text('Results from the load test pipeline will be displayed here')


    #chromium_page_with_state.wait_for_timeout(5000)