from playwright.sync_api import Page

from components.base_component import BaseComponent


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.estimated_time = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.description = page.get_by_test_id('create-course-form-description-input').locator('input')
        self.max_scor = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.min_score = page.get_by_test_id('create-course-form-min-score-input').locator('input')

    def fill_form(self, estimatsd_time: str, description: str, max_score: str, min_score: str):
