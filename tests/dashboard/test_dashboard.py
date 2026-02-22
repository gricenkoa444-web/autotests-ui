from pages.dashboard.dashboard_page import DashboardPage
import pytest


@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        dashboard_page_with_state.navbar.check_visible(' test_username!')
        dashboard_page_with_state.sidebar_component.check_visible()



