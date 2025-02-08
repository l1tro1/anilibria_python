from behave import step
from selenium.common import NoSuchElementException


@step('открываю фильтр около поля "поиск"')
def open_search_filter(context):
    """
        Шаг для открытия фильтра рядом с полем поиска.

        Args:
            context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                    Включает current_page для работы с текущей страницей.

        Steps:
            1. Получает текущую страницу из контекста.
            2. Открывает фильтр рядом с полем поиска.

        Returns:
            None
    """
    try:
        page = context.current_page
        page.search_filter_button.open()
    except Exception as e:
        context.logger.error(f"Ошибка открытия фильтра {e}")
        raise


@step('выставляю в фильтре в секции "{section_name}" значение "{values}"')
def fill_filter(context, section_name, values):
    """
    Шаг для установки значения в фильтре в указанной секции.

    Args:
        context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                Включает current_page для работы с текущей страницей.
        section_name (str): Название секции фильтра.
        values (str): Значение или диапазон значений для установки в фильтре.

    Steps:
        1. Получает текущую страницу из контекста.
        2. Находит секцию фильтра по названию.
        3. Если values содержит дефис ('-'), интерпретирует его как диапазон и устанавливает ползунок.
        4. Иначе находит кнопку по значению и кликает по ней.

    Returns:
        None
    """
    page = context.current_page
    filter_part = page.search_filter.filters.part_by_title(section_name)
    if '-' in values:
        try:
            filter_part.slide_to_range(values)
        except Exception as e:
            context.logger.error(f"Не удалось выставить диапазон {values} в фильтре с ошибкой {e}")
            raise
    else:
        button = filter_part.button_by_name(values)
        if button is None:
            raise NoSuchElementException(f'Кнопка {values} в секции {section_name} не найдена')
        button.click()
    page.wait_load()


@step('нажимаю кнопку "{button_name}" в фильтре')
def click_filter_button(context, button_name):
    """
    Шаг для нажатия кнопки в фильтре.

    Args:
        context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                Включает current_page для работы с текущей страницей.
        button_name (str): Название кнопки, которую нужно нажать.

    Steps:
        1. Получает текущую страницу из контекста.
        2. Находит кнопку по названию.
        3. Если кнопка найдена, кликает по ней.
        4. Ожидает загрузки страницы.

    Returns:
        None
    """
    page = context.current_page
    button = page.search_filter.button_by_name(button_name)
    if button is None:
        raise NoSuchElementException(f'Кнопка с именем {button_name} не найдена')
    button.click()
    page.wait_load()
