
from playwright.sync_api import sync_playwright, expect

# Создали открытие сайта 1-launch запускает chromium 2-headless=False такой командой мы хотим показать, что страница
# должна отбражаться на экране, а не выполняться по умолчанию () 3-создали новуюстраницу chromium.new_page()- дали ей
# нименование page и запустили это страницу page.goto с указаным сайтом
# контекстный менеджер будет сам закрывать браузер нам не нужно дополнительно прописывать команду chromium.close()
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

#далее по плану провеки собираемся ввести данные в окна (для начала мы ищем на сайте XPATH)
#создаем переменную email_input для того, что бы дальше работать с докатором
#далее локатер по переменной email_input добавляем fill - для заполнения данными определенное поле
    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill('user.name@gmail.com')
# далее нам нужно заполнить данными пароль, производим теже манипуляции что и юзернейм
    password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill('password')
# нажимаем кнопку логин
    login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()
#проверим элемент visible
    wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible()
#проверим что он содежит определнный тектс
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

# Просим playwright подождать 5 секунт для того, что бы мы могли увидеть все действия, так как он все очень быстро
# делает используется только для демо. в реальных проектах - неиспользовать ни time.sleep - плохо так как это
# неявные ожидания, они тормозят наш тест (нет причин использовать такой слип неявно для чего)
    page.wait_for_timeout(5000)


