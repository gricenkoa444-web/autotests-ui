import pytest
# автоматический запуск функции (не нужно запускать руками) - это возможно с помощью указанного декоратора fixture(
# autouse=True)
@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервис аналикти")

# settings - обычно имеет scope="session" scope - параметр у которого есть пул значений [session, package,module,class,
# function] session - самый глобальный скоруп, будет запущена один раз на всю тестовую сессию package - пакет в
# питоне это папка в нутри которой есть __init__ файл - фикстура package будет запущена один раз на весь пакет(прогон
# всей папки имеющей инит)
# module - один файл (фикстару с таким пулом будет запущена один раз на весь файл )
# class - один раз на весь тестовый класс
# function - одни раз на тестовую функцию

# если мы припишем декоратор @pytest.fixture по дефолту - будет function
@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициализируем настройки автотестов")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")

# function - указывать не обязательно - по дефолту все равно будет function
@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Октрываем браузер на каждый автотест")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...