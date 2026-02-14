import pytest
from playwright.sync_api import Page, expect
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage

title = "Playwright"
estimated_time = "2 weeks"
description = "Playwright"
max_score = "100"
min_score = "10"


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title = "",
        description = "",
        estimated_time = "",
        max_score = "0",
        min_score = "0"
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image(file = "./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(
        title=title,
        estimated_time=estimated_time,
        description=description,
        max_score=max_score,
        min_score=min_score
    )
    create_course_page.click_create_course_button()



    courses_list_page.check_visible_courses_title()

    courses_list_page.chek_visible_create_course_button()

    courses_list_page.check_visible_course_card(
        index=0,
        title=title,
        max_score=max_score,
        min_score=min_score,
        estimated_time=estimated_time
    )




