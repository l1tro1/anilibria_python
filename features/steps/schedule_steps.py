import calendar
import datetime
import re

# Нужно для работы equal
import sure
from behave import step
from selenium.common import NoSuchElementException

from features.support.logger import check_element


@step('я должен увидеть в разделе breadcrumbs путь "{breadcrumb_page}"')
def check_breadcrumbs(context, breadcrumb_page):
    """
    Шаг для проверки наличия указанного пути в разделе breadcrumbs.

    Args:
        context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                Включает current_page для работы с текущей страницей и logger для логирования.
        breadcrumb_page (str): Ожидаемый путь (текст), который должен отображаться в breadcrumbs.

    Steps:
        1. Получает текущую страницу из контекста.
        2. Находит элемент breadcrumbs по тексту, указанному в breadcrumb_page.
        3. Проверяет, что элемент существует и видим на странице.
        4. Сравнивает текст элемента с ожидаемым значением breadcrumb_page.
        5. Логирует успешное выполнение шага.

    Returns:
        None
    """
    current_page = context.current_page
    breadcrumb = current_page.breadcrumbs.element_by_text(breadcrumb_page)
    check_element(breadcrumb, breadcrumb_page)

    breadcrumb_text = breadcrumb.text
    breadcrumb_text.should.equal(breadcrumb_page)
    context.logger.info(f"Путь '{breadcrumb_page}' найден в breadcrumbs")


@step('я должен увидеть в описании страницы {part}')
def check_description_title(context, part):
    """
       Шаг для проверки текста в указанной части описания страницы.

       Args:
           context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                   Включает current_page для работы с текущей страницей, text для ожидаемого текста
                   и logger для логирования.
           part (str): Название части описания страницы, которую нужно проверить.
                      Например, "заголовок" или "подзаголовок".

       Steps:
           1. Преобразует part в формат, подходящий для поиска атрибута на странице.
           2. Получает текущую страницу из контекста.
           3. Находит элемент в описании страницы по указанной части.
           4. Сравнивает текст элемента с ожидаемым значением из context.text.
           5. Логирует успешное выполнение шага.

       Returns:
           None
    """
    page_part = _page_part(part)
    current_page = context.current_page
    element = getattr(current_page.description, page_part)
    element.text.should.equal(context.text)
    context.logger.info(f"{part.title()} описания страницы совпадает с ожидаемым")


@step('я ввожу в поле "{field}" текст "{text}"')
def test_step(context, field, text):
    """
    Шаг для ввода текста в указанное поле на странице.

    Args:
        context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                Включает current_page для работы с текущей страницей и logger для логирования.
        field (str): Название поля, в которое нужно ввести текст.
        text (str): Текст, который нужно ввести в поле.

    Steps:
        1. Получает текущую страницу из контекста.
        2. Очищает поле ввода.
        3. Обрабатывает текст.
        4. Логирует текст, который будет введен в поле.
        5. Вводит текст в поле.
        6. Ожидает загрузки страницы после ввода текста.

    Returns:
        None
    """
    page = context.current_page
    # @see features/support/monkeypatch/webdriver
    page.search_field.clear_input()
    text = _eject_release_num(context, text)

    context.logger.info(f'Текст для ввода в поле "{field}" - "{text}"')
    page.search_field.send_keys(text)
    page.wait_load()


@step('я должен увидеть в результате поиска "{part}"')
def check_search_result(context, part):
    """
    Шаг для проверки текста в указанной части результатов поиска.

    Args:
        context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                Включает current_page для работы с текущей страницей, text для ожидаемого текста
                и logger для логирования.
        part (str): Название части результатов поиска, которую нужно проверить.
                   Например, "заголовок" или "описание".

    Steps:
        1. Преобразует part в формат, подходящий для поиска атрибута на странице.
        2. Получает текущую страницу из контекста.
        3. Находит элемент в результатах поиска по указанной части.
        4. Сравнивает текст элемента с ожидаемым значением из context.text.
        5. Логирует успешное выполнение шага.

    Returns:
        None
    """
    page_part = _page_part(part)

    page = context.current_page
    element = getattr(page.failed_search_result, page_part)
    element.text.should.equal(context.text)
    context.logger.info(f"{part.title()} результатов поиска страницы совпадает с ожидаемым")


@step('я должен увидеть в успешном результате поиска "{part}" текст "{message}"')
def check_success_search_result(context, part, message):
    """
     Шаг для проверки текста в указанной части успешного результата поиска.

     Args:
         context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                 Включает current_page для работы с текущей страницей.
         part (str): Название части результата поиска, которую нужно проверить.
                    Например, "заголовок" или "описание".
         message (str): Ожидаемый текст, который должен содержаться в указанной части.

     Steps:
         1. Преобразует part в формат, подходящий для поиска атрибута на странице.
         2. Получает текущую страницу из контекста.
         3. Обрабатывает message, заменяя возможные плейсхолдеры (например, номер релиза).
         4. Итерирует по всем успешным результатам поиска на странице.
         5. Проверяет, содержит ли указанная часть (part) ожидаемый текст (message).
         6. Если текст найден, завершает выполнение.
         7. Если текст не найден, выбрасывает исключение NoSuchElementException.

     Raises:
         NoSuchElementException: Если элемент с указанным текстом не найден.

     Returns:
         None
    """
    page_part = _page_part(part)
    page = context.current_page
    search_result = None
    message = _eject_release_num(context, message)

    for success_search in page.success_search_results:
        element = getattr(success_search, page_part)
        if element.text == message:
            search_result = element.text
            break
    if search_result is None:
        raise NoSuchElementException(f'Элемент с {part} равным "{message}" не найден')


@step('получаю информацию о релизах за "{day}" на UI')
def collect_release_info_ui(context, day):
    """
    Шаг для сбора информации о релизах за указанный день на пользовательском интерфейсе.

    Args:
        context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                Включает current_page для работы с текущей страницей и logger для логирования.
        day (str): День, за который нужно собрать информацию. Может быть "сегодня" или конкретный день недели.

    Steps:
        1. Определяет текущий день (если day == "сегодня", использует текущий день недели).
        2. Логирует выбранный день.
        3. Получает текущую страницу из контекста.
        4. Находит и кликает по кнопке, соответствующей выбранному дню.
        5. Ожидает загрузки страницы.
        6. Собирает информацию о релизах из карточек на странице.
        7. Логирует количество найденных релизов.
        8. Сохраняет собранную информацию в контексте.

    Returns:
        None
    """
    if day == 'сегодня':
        current_day = calendar.day_name[datetime.datetime.today().weekday()]
    else:
        current_day = day
    context.logger.info(f"День для поиска выбран: {current_day}")
    page = context.current_page
    day_button = page.day_by_name(current_day)
    day_button.click()
    page.wait_load()
    info = []
    for card in page.cards:
        splits_info = card.text.split("\n")
        info.append({"name": splits_info[0], "episode": splits_info[1], "genre": splits_info[3]})

    context.logger.info(f'Найдено {len(info)} релизов.')
    context.anime_releases = info


@step('я должен увидеть "{count}" результат успешного поиска')
def check_count_success_search(context, count):
    """
    Шаг для проверки количества результатов успешного поиска.

    Args:
        context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                Включает current_page для работы с текущей страницей.
        count (str): Ожидаемое количество результатов поиска.

    Steps:
        1. Получает текущую страницу из контекста.
        2. Проверяет, что количество результатов успешного поиска равно ожидаемому значению.

    Returns:
        None
    """
    try:
        page = context.current_page
        actual_count =  len(page.success_search_results)
        actual_count.should.equal(int(count))
        context.logger.info(f"Количество результатов успешного поиска: {actual_count} (ожидалось: {count})")
    except AssertionError as e:
        context.logger.error(f"Количество результатов не совпадает с ожидаемым: {e}")
        raise
    except Exception as e:
        context.logger.error(f"Ошибка при проверке количества результатов поиска: {e}")
        raise RuntimeError(f"Ошибка при проверке количества результатов поиска: {e}")


@step('очищаю поле поиска')
def clear_search_field(context):
    """
    Шаг для очистки поля поиска на текущей странице.

    Args:
        context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                Включает current_page для работы с текущей страницей.

    Steps:
        1. Получает текущую страницу из контекста.
        2. Очищает поле поиска с помощью метода clear_input().

    Returns:
        None
    """
    page = context.current_page
    page.search_field.clear_input()


def _page_part(part: str) -> str:
    expected_parts = {'заголовок': 'title',
                      'подзаголовок': 'subtitle',
                      'тело': 'body'}
    page_part = expected_parts.get(part)
    check_element(page_part, part)
    return page_part


def _eject_release_num(context, message: str) -> str:
    custom_text = re.compile(r"^имя (\d+) релиза из списка$")
    if custom_text.match(message):
        if context.anime_releases is None:
            raise AttributeError("Список релизов не заполнен.")
        num = int(custom_text.match(message)[1])
        message = context.anime_releases[num - 1]['name']
    return message
