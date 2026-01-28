from playwright.sync_api import sync_playwright, expect, Request, Response
#две функции которые будут обрабатывать запрос и ответ (callback)

def log_request(request: Request):
    print(f'Request: {request.url}')


def log_response(response: Response):
    print(f'Response: {response.url}, {response.status}')



#Перехват запроса и ответа от сервака
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
#добавляем обработчик page.on
    page.on('request', log_request)  #Запрос
#удаляем обработчик
    #page.remove_listener('request', log_request)
    page.on('response', log_response) #Ответ

    page.wait_for_timeout(5000)
# В автотестах это нужно для вербозности, логировать больше данных - в случае подения теста удобнее искать ошибки
# Таким же путем можно проверять статусы кода ответа, пример: {response.status}

