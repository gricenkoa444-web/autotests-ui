from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('create-course-toolbar-title-text')
        self.button = page.get_by_test_id('create-course-toolbar-create-course-button')

    def check_visible(self, is_create_course_disabled: bool = True) -> None:
        expect(self.title).to_be_visible()

        expect(self.button).to_be_visible()

        if is_create_course_disabled:
            expect(self.button).to_be_disabled(timeout=6000)
        else:
            expect(self.button).to_be_enabled(timeout=6000)

    def click(self) -> None:
        self.button.click()


