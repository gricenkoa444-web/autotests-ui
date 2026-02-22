## 🎭 UI Automation Testing Framework

![](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80)
*<small>Автоматизация тестирования с Playwright + Pytest + PageObject</small>*

### 📋 О проекте

Фреймворк для автоматизированного UI-тестирования веб-приложений с использованием современных подходов и паттернов проектирования.

### 🏗️ Архитектура

Проект построен на комбинации трех ключевых паттернов:

| Паттерн | Назначение |
|---------|------------|
| **PageObject** | Инкапсуляция логики страниц (`pages/`) |
| **PageComponent** | Переиспользуемые UI-компоненты (`components/`) |
| **PageFactory** | Базовые элементы (`elements/`) |

### 🛠️ Tech Stack

![Playwright](https://img.shields.io/badge/-Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/-Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)

# Установка зависимостей
pip install -r requirements.txt
playwright install

# Запуск всех тестов с маркировкой regression
python -m pytest -s -v -m "regression"