from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.icon import Icon
from elements.text import Text
import allure

class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.empty_icon = Icon(page, f'{identifier}-empty-view-icon', f'Icon')
        self.empty_title = Text(page, f'{identifier}-empty-view-title-text', f'Title')
        self.empty_description = Text(
            page, f'{identifier}-empty-view-description-text', 'Description'
        )
    @allure.step('Check visible empty view "{title}"')
    def check_visible(self, title: str, description: str):
        self.empty_icon.check_visible()

        self.empty_title.check_visible()
        self.empty_title.check_have_text(title)

        self.empty_description.check_visible()
        self.empty_description.check_have_text(description)

