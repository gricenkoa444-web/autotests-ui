from pages.base_page import BasePage
from playwright.sync_api import Playwright, Page, expect


class CourseListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    # Title and button for create course
        self.courses_title =page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

    # Empty block if there are no courses
        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')

    # Title and button "Create course"
        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.disabled_create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')


    # Course Card empty
        self.preview_empty_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.preview_empty_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.preview_empty_description = page.get_by_test_id('create-course-preview-empty-view-description-text')

    # Image Card empty
        self.preview_image_upload_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.preview_image_upload_title = page.get_by_test_id(
            'create-course-preview-image-upload-widget-info-title-text'
        )
        self.preview_image_upload_description = page.get_by_test_id(
            'create-course-preview-image-upload-widget-info-description-text'
        )
        self.preview_image_upload_button = page.get_by_test_id(
            'create-course-preview-image-upload-widget-upload-button'
        )


    # Course Card with image
        self.preview_image_remove_button = page.get_by_test_id(
            'create-course-preview-image-upload-widget-remove-button'
        )
        self.preview_image_upload_widget = page.get_by_test_id(
            'create-course-preview-image-upload-widget-preview-image'
        )

    # Create Course Form
        self.title_form_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.estimated_time_form_input = page.get_by_test_id('create-course-form-estimated-time-input').locator(
            'input'
        )
        self.description_form_input = page.get_by_test_id('create-course-form-description-input').locator('textarea')
        self.max_score_form_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.min_score_form_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

    # Exercises Box
        self.exercises_box_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.exercises_box_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')
        self.exercises_empty_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.exercises_empty_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.exercises_empty_description = page.get_by_test_id('create-course-exercises-empty-view-description-text')

    # Create Exercises Course
        self.exercises_subtitle_text = page.get_by_test_id('create-course-exercise-0-box-toolbar-subtitle-text')
        self.exercises_title_form_input = page.get_by_test_id('create-course-exercise-form-title-0-input').locator('input')
        self.exercises_description_form_input = page.get_by_test_id('create-course-exercise-form-description-0-input')

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        expect(self.empty_view_icon).to_be_visible()

        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text('There is no results')

        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')

    def chek_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

    def check_visible_disabled_create_course_button(self):
        expect(self.disabled_create_course_button).to_be_visible()
        expect(self.disabled_create_course_button).to_be_disabled()

    def click_disabled_create_course_button(self):
        expect(self.disabled_create_course_button).not_to_be_clickable()

    def check_visible_course_card(self):
        expect(self.preview_empty_icon).to_be_visible()

        expect(self.preview_empty_title).to_be_visible()
        expect(self.preview_empty_title).to_have_text('No image selected')

        expect(self.preview_empty_description).to_be_visible()
        expect(self.preview_empty_description).to_have_text('Preview of selected image will be displayed here')

    def check_visible_image_upload_card(self):
        expect(self.preview_image_upload_icon).to_be_visible()

        expect(self.preview_image_upload_title).to_be_visible()
        expect(self.preview_image_upload_title).to_have_text('Tap on "Upload image" button to select file')

        expect(self.preview_image_upload_description).to_be_visible()
        expect(self.preview_image_upload_description).to_have_text('Recommended file size 540X300')

        expect(self.preview_image_upload_button).to_be_visible()

    def check_visible_create_course_form(self):
        expect(self.title_form_input).to_be_visible()
        expect(self.title_form_input).to_have_value(title)







