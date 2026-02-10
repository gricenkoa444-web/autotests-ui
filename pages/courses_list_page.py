from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')

        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')
        self.preview_empty_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.preview_empty_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.preview_empty_description = page.get_by_test_id('create-course-preview-empty-view-description-text')
        self.preview_image_upload_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.preview_image_upload_text = page.get_by_test_id(
            'create-course-preview-image-upload-widget-info-title-text'
        )
        self.preview_image_upload_description = page.get_by_test_id(
            'create-course-preview-image-upload-widget-info-description-text'
        )
        self.preview_image_upload_button = page.get_by_test_id(
            'create-course-preview-image-upload-widget-upload-button'
        )
        self.title_form_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.estimated_time_input = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.description_form_input = page.get_by_test_id('create-course-form-description-input').locator('input')
        self.create_form_max_input = page.get_by_test_id('create-course-form-max-score-input')
        self.create_form_min_input = page.get_by_test_id('create-course-form-min-score-input')


        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')
        self.hidden_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        self.create_exercises_text = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercises_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')
        self.exercises_empty_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.exercises_empty_text = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.exercises_empty_suscriotions_text = page.get_by_test_id(
            'create-course-exercises-empty-view-description-text'
        )


    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        expect(self.empty_view_icon).to_be_visible()

        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_heva_text('There is no results')

        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text(
            'Results from the load test pipeline will be displayed here'
        )

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        expect(self.create_course_button).click()








