import pytest

@pytest.mark.smoke
def test_smoke_case():
    ...


@pytest.mark.regression
def test_regression_case():
    ...

#в данном случае, мы можем запустить марикровку на весь класс и в нем может находтится разные варианты кейсов
#и также можно присвоить маркировку к каждой функции поотрдельности как указано выше
@pytest.mark.smoke
class TestSuite:
    def test_suite(self):
        ...

    def test_tests(self):
        ...

 # маркировки нам нужны для того что бы базово пометь какие либо тесты, за какую  функциональность отвечают,
# сгрупировать их по группам (разгроничение) и плюс не нужно знать название тестов


@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_password(self):
        ...


    def test_logout(self):
        ...


# что бы запустить по определенной последовательности pytest мы будем использовать в терминале команду "regression
# and slow" в таком случае запустятся тесты, котрые содердат и regression и slow - все что не будет содержать и одно
# и второе -не запустится


# тестовый класс и тестовая функция может иметь несколько маркировок
# при запуске тестов, она будет подходит под любую из указанных маркировок - гибкий вариант маркировок

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.critical
def test_critical():
    ...
