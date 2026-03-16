from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_data = {
    'id': 1,
    'username': 'john_doe',
    'email': 'jhon90@gmail.com'
}


user = User(**user_data)
print(user)
print(user.is_active)

# Пример валидации данных при создании экземпляра модели
invalid_user_data = {
    'id': 'two',
    'username': 'jane_doe',
    'email': ''
}
try:
    invalid_user = User(**invalid_user_data)
except Exception as error:
    print('Ошибка валидации данных:', error)