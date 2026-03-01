from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import allure
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.text import Text
from elements.image import Image


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.title = Text(page, 'course-widget-title-text', 'Title')
        self.image = Image(page, 'course-preview-image', 'PreviewImage')
        self.max_score = Text(page, 'course-max-score-info-row-view-text', 'Max Score')
        self.min_score = Text(page, 'course-min-score-info-row-view-text', 'Min Score')
        self.estimated_time = Text(page, 'course-estimated-time-info-row-view-text', 'Estimated Time')

    @allure.step('Check visible course view at index "{index}"')
    def check_visible(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score:str,
            estimated_time: str
    ):
        #expect(self.image.nth(index)).to_be_visible()
        self.image.check_visible(nth=index)

        #expect(self.title.nth(index)).to_be_visible()
        #expect(self.title.nth(index)).to_have_text(title)
        self.title.check_visible(nth=index)
        self.title.check_have_text(title, nth=index)

        #expect(self.max_score.nth(index)).to_be_visible()
        #expect(self.max_score.nth(index)).to_have_text(f'Max score: {max_score}')
        self.max_score.check_visible(nth=index)
        self.max_score.check_have_text(f'Max score: {max_score}', nth=index)

        #expect(self.min_score.nth(index)).to_be_visible()
        #expect(self.min_score.nth(index)).to_have_text(f'Min score: {min_score}')
        self.min_score.check_visible(nth=index)
        self.min_score.check_have_text(f'Min score: {min_score}', nth=index)

        #expect(self.estimated_time.nth(index)).to_be_visible()
        #expect(self.estimated_time.nth(index)).to_have_text(f'Estimated time: {estimated_time}')
        self.estimated_time.check_visible(nth=index)
        self.estimated_time.check_have_text(f'Estimated time: {estimated_time}', nth=index)


