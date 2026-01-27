from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Запускаем Chromium
    browser = p.chromium.launch(headless=False)  # headless=False чтобы видеть окно
    page = browser.new_page()
    page.goto("https://google.com")
    print(f"Открыта страница: {page.title()}")
    browser.close()