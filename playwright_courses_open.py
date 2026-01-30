from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser_one_test-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    button_courses_click = page.get_by_test_id('courses-drawer-list-item-button')
    button_courses_click.click()

    label_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(label_courses).to_be_visible()
    expect(label_courses).to_have_text('Courses')
    print('1.Test is ok')

    block_there_is_no_result = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(block_there_is_no_result).to_have_text('There is no results')
    print('2.Test is ok')

    file_visible = page.get_by_test_id('courses-list-empty-view-icon')
    expect(file_visible).to_be_visible()
    print('3.Test is ok')

    block_results_from_the_load = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_results_from_the_load).to_be_visible()
    expect(block_results_from_the_load).to_have_text('Results from the load test pipeline will be displayed here')
    print('4.Test is ok')

    page.wait_for_timeout(5000)