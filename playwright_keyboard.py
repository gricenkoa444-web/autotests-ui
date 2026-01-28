from playwright.sync_api import sync_playwright, expect

#Имуляция нажатия кнопок(для специфичных полей ввода) Ctrl + A
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False) #иницилизируем браузер
    page = browser.new_page() #иницилизируем новую страницу

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    #вызываем метод focus
    login_email_input.focus()
    #после того как сфокусировались на поле, можем печать с клавиатуры

# for каждой буквы в 'user@gmail.com' - страница(page = browser.new_page()) используем keyboard.type - клавиатура
# печатает. type может принимать параметр delay - задержка по вперемни при печати, что бы видеть визуально,
# как он печатает каждый символ.
    for char in 'user@gmail.com':
        page.keyboard.type(char, delay=300)

    page.keyboard.press('ControlOrMeta+A')

    page.wait_for_timeout(5000)

# Теперь выполняем нашу задачу иницилизации нажатия кнопок на клавиатуре (keyboard) Ctrl + A выделение текста
# page.keyboard.press('ControlOrMeta+A') - универсальная команда подходит для видны и для макос

#press используется для нажатия клавишь
#type используетс для обычной печати, без сложных комбинаций