import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, 4, -1])
def test_numbers(number: int):
    assert number > 0
    #print(f"Number: {number}")

@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9), (4, 12)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

# Перемножение параметров
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
@pytest.mark.parametrize('os', ['macOS', 'windows', 'linux', 'debian'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


# Параметризация Фикстуры
@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param

# Используем фикстуру в тесте

def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')

# Используем параметрайз в классе
@pytest.mark.parametrize('user', ['Alice', 'Bob'])
class TestOperation:
    #@pytest.mark.parametrize('user', ['Alice', 'Bob'])
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operation(self, user: str, account: str):
        ...

    #@pytest.mark.parametrize('user', ['Alice', 'Bob'])
    def test_user_without_operation(self, user: str):
        ...

# Идентификаторы параметрайз  ids=['...', '...']
@pytest.mark.parametrize(
    'phone_number',
    ['+7900000000', '+79000887711'],
    ids=[ # не изменяем
         'user with money on bank account',
         'user without money on bank account'
    ]
)
def test_identifiers(phone_number: str):
    ...


# Дминамическое формирование индентификатора ( более емкий вариант кода )

user ={
    '+7900000000': 'user with money on bank account',
    '+79000887711': 'user without money on bank account'
}

@pytest.mark.parametrize(
    'phone_number',
     user.keys(),
    # Можем использовать функцию но это избыточно, пример ( см скрипт ниже format_phone_number)
    #ids=format_phone_number # передаем саму функцию - работает так же как и лямбда

    # используем контекстную функцию lambda
    # можно передать либо функцию, либо список - что удобнее то и делаем
    ids=lambda phone_number: f'{phone_number}: {user[phone_number]}'# Работает динамическое форматирование
)

def test_identifiers_1(phone_number: str):
    print('Динамическое формирование идентификаторов')


# Обычная функция





