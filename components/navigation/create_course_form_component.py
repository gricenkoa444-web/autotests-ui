from playwright.sync_api import Page, expect


class CreateCourseFormComponent:
    def __init__(self, page):
        self.page = page

        self.title_input = page.get_by_test_id('')

