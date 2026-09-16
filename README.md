# Magic_UI

UI-автотесты для демо-магазина [testshop.qa-practice.com](http://testshop.qa-practice.com) на Python.

## Стек
- Python
- Pytest
- Selenium
- Page Object Model (POM)
- Allure
- GitHub Actions

## Что покрыто
- Открытие карточки товара
- Добавление товара в корзину
- Проверка количества в корзине
- Текст заголовка корзины и сообщения о пустой корзине
- Проверка Terms and Conditions
- Страница каталога (desks)

## Структура проекта

- `pages/` — Page Object'ы (base, product, basket, desks)
- `pages/locators/` — локаторы
- `tests/` — тест-кейсы
- `conftest.py` — фикстура драйвера (headless Chrome)
- `pytest.ini` — настройки pytest
- `.github/workflows/` — CI (запуск тестов)

## Запуск

1. Установи зависимости:

```bash
pip install -r requirements.txt