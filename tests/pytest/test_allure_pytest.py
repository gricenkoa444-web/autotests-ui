import allure


def test_feature():
    with allure.step('Check displaying dashboard'):
        ...

    with allure.step('Creating course'):
        ...

    with allure.step('Closing browser'):
        ...

    # Контекстный менеджер в Python — это объект, который управляет ресурсами (файлами, соединениями с БД, блокировками, временными директориями и т.д.) с помощью конструкции with.
    # Главное преимущество — гарантированное выполнение cleanup-кода даже при исключениях.