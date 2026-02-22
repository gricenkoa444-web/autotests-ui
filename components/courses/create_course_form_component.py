from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Input(page, 'create-course-form-title-input', 'Title Form')
        self.estimated_time = Input(page, 'create-course-form-estimated-time-input', 'Estimated Form')
        self.description = Input(page, 'create-course-form-description-input', 'Description Form')
        self.max_score = Input(page, 'create-course-form-max-score-input', 'Max Score Form')
        self.min_score = Input(page, 'create-course-form-min-score-input', 'Min Score Form')

    def fill_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title.fill(title)
        self.estimated_time.fill(estimated_time)
        self.description.fill(description)
        self.max_score.fill(max_score)
        self.min_score.fill(min_score)

    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title.check_visible()
        self.title.check_have_text(title)

        self.estimated_time.check_visible()
        self.estimated_time.check_have_text(estimated_time)

        self.description.check_visible()
        self.description.check_have_text(description)

        self.max_score.check_visible()
        self.max_score.check_have_text(max_score)

        self.min_score.check_visible()
        self.min_score.check_have_text(min_score)
