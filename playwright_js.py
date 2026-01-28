from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
        wait_until='networkidle'
    )


 # evaluate = запускает js код
 # В данном примере текст захаткоженный - можно это измнить (см ниже)
    page.evaluate(
        """
        const titel = document.getElementById('authentication-ui-course-title-text')
        titel.textContent = 'New Text'
        """
    )


    text = 'New Text'
    page.evaluate(
        f"""
        const titel = document.getElementById('authentication-ui-course-title-text')
        titel.textContent = '{text}'
        """
    )

    page.wait_for_timeout(5000)

#НЕ Произойдет изменение текст контент в авто режиме, тоже самое что мы бы в консоли прописывали в девтулс
#Здесь производится работа с JS - для нее нужны необходимы загрузки файлов ждать

#Скрипт не отпработал из-за того, что когда открылась страница с помощью page.evaluate - js, chunk еще не загрузтлись
#Фактически мы выполняем скрипт - на пустой странице, на момент запуска кода и открытия страницы там есть пустой файл

#что бы скрипт отработал, нужно прописать ожидание в скрипте в самом
# page.goto  - wait_until='networkidle' ждем загрузку Network - произойдет полныя загрузка файлов и после этого отр скр