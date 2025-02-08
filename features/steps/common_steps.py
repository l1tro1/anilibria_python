from behave import step


@step('я открываю браузер')
def open_browser(context):
    """
       Шаг для открытия браузера и загрузки главной страницы.

       Args:
           context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                   Включает page_factory для создания страниц.

       Steps:
           1. Устанавливает имя страницы как 'Главная'.
           2. Создает экземпляр главной страницы с помощью page_factory.
           3. Загружает страницу.
           4. Ожидает полной загрузки страницы.
           5. Сохраняет текущую страницу в контексте.

       Returns:
           None
    """
    context.page_name = 'Главная'
    _load_page(context, 'Главная')


@step('я открываю браузер на странице "{page_name}"')
def open_browser_on_page(context, page_name):
    """
        Шаг для открытия браузера и загрузки указанной страницы.

        Args:
            context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                    Включает page_factory для создания страниц.
            page_name (str): Название страницы, которую нужно открыть.

        Steps:
            1. Устанавливает имя страницы из аргумента page_name.
            2. Создает экземпляр страницы с помощью page_factory.
            3. Загружает страницу.
            4. Ожидает полной загрузки страницы.
            5. Сохраняет текущую страницу в контексте.

        Returns:
            None
        """
    context.page_name = page_name
    _load_page(context, page_name)


@step('я перехожу в раздел "{page}"')
def open_page(context, page):
    """
        Шаг для перехода в указанный раздел на текущей странице.

        Args:
            context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
                    Включает current_page для работы с текущей страницей.
            page (str): Название раздела, в который нужно перейти.

        Steps:
            1. Получает текущую страницу из контекста.
            2. Находит кнопку перехода в раздел по имени.
            3. Кликает по кнопке.
            4. Устанавливает имя страницы как название раздела.
            5. Создает экземпляр новой страницы с помощью page_factory.
            6. Загружает новую страницу.
            7. Ожидает полной загрузки страницы.
            8. Сохраняет текущую страницу в контексте.

        Returns:
            None
    """
    current_page = context.current_page
    button = current_page.header.navigation.button_by_name(page)
    button.click()
    context.page_name = page
    _load_page(context, page)


def _load_page(context, page_name):
    """
        Вспомогательная функция для загрузки страницы.

        Args:
            context: Контекст выполнения теста.
            page_name (str): Название страницы для загрузки.

        Raises:
            AttributeError: Если context не содержит page_factory.
            RuntimeError: Если страница не загрузилась.

        Returns:
            None
    """
    if not hasattr(context, 'page_factory'):
        raise AttributeError("Контекст не содержит page_factory.")
    try:
        page = context.page_factory(context)
        page.load()
        page.wait_load()
        context.current_page = page
    except Exception as e:
        raise RuntimeError(f"Ошибка при загрузке страницы '{page_name}': {e}")
