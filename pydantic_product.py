from pydantic import BaseModel, Field, ValidationError

class Market(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description='Цена должна быть больше 0')
    tags: list[str] = []
    market: Market

# Работа со словаремданых для создание экземпляра модели
product_data = {
    'name': 'Laptop',
    'price': 999.99,
    'tags': ['electronics', 'computers'],
    'market': {
        'id': 1,
        'name': 'Tech Store'
    }
}

product = Product(**product_data)
print(product)

# Работа с объектом модели
new_product = Product(
    name='Home',
    price=999.90,
    tags=['electronics', 'home applications'],
    market=Market(id=2, name='Home Store')
)
print('new_product', new_product)