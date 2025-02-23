# Anilibria Python

Репозиторий содержит автотесты для сайта https://anilibria.top/
Реализованы лишь базовые сценарии для демонстрации навыков.
## Тестирование UI
Использован паттерн PageObject.
Для его реализации позаимствована идея https://github.com/site-prism/site_prism

Доработана реализация этой идеи на Python https://github.com/l1tro1/py_prism

Технологии:
- Selenium
- GoogleChrome
- Behave
### Расположение UI тестов
 ```bash
  anilibria_python/features/tests/release_page
  anilibria_python/features/tests/schedule_page
 ```

## Тестирование REST API
Использована библиотека **requests**
Создана обертка для хранения и поиска Endpoint. Создана обертка для выполнения REST запросов.
Добавлена библиотека jsonschema для валидации ответов на предмет соответствия схеме.
### Расположение REST API тестов
 ```bash
  anilibria_python/features/tests/api
 ```
## Тестирование собственного кода
Использована библиотека **pytest**
### Расположение pytest тестов
 ```bash
  anilibria_python/pytest
 ```

## Особенности
- Доработан **selenium.webdriver.remote.webelement**. Добавлены методы получения xpath элемента и очистки поля ввода.
- Доработан **logger**. Добавлена цветовая индикация уровня логирования.
- Страницы разделены на секции для удобства переиспользования и упрощения изменения автотестов при смене верстки
