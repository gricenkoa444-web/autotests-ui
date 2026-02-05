import pytest

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




