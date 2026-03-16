from playwright.sync_api import Page, expect
import allure
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page,'create-course-exercises-box-toolbar-title-text', 'Title')
        self.button = Button(
            page, 'create-course-exercises-box-toolbar-create-exercise-button', 'Create Exercises'
        )

    @allure.step('Check visible create course {title}')
    def check_visible(self):
        self.title.check_visible()

        self.button.check_visible()

    def click_button(self):
        self.button.click()