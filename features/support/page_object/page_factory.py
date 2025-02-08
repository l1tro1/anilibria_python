import re


class PageFactory:
    """
        Класс, который управляет страницами и их загрузками.

        Конструктор принимает два аргумента:
        - pages: Словарь, где ключи — это имена страниц, а значения — это локаторы для поиска.
        - loaders: Словарь, где ключи — это имена страниц, а значения — это функции для загрузки страниц.
    """

    def __init__(self, pages, loaders, driver):
        """
        Инициализирует объект PageFactory с переданными страницами и загрузчиками.

        :param pages: Словарь с локаторами для страниц.
        :param loaders: Словарь с функциями для загрузки страниц.
        """
        self.pages = pages
        self.loaders = loaders
        self.loaded_pages = {}
        self.driver = driver

    def page_at(self, text_locator):
        """
        Ищет страницу, соответствующую переданному локатору текста.

        Метод проверяет локаторы для каждой страницы и возвращает соответствующую
        страницу, если она найдена. В случае, если страница не найдена, вызывает исключение KeyError.

        :param text_locator: Локатор текста, который используется для поиска страницы.
        :return: Загрузившаяся страница.
        :raises KeyError: Если страница с таким локатором не найдена.
        """
        for key, locators in self.pages.items():
            if self._matches_locator(locators, text_locator):
                return self._load_page(key)

        raise KeyError(f'Не найден ключ для локатора "{text_locator}"')

    def _matches_locator(self, locators, text_locator):
        """
        Проверяет, совпадает ли переданный локатор с локаторами для страницы.

        Метод сначала ищет совпадения с регулярными выражениями, а затем проверяет
        точное совпадение с текстовыми локаторами.

        :param locators: Локаторы, связанные с данной страницей (строки или регулярные выражения).
        :param text_locator: Локатор текста, который нужно найти.
        :return: True, если найдено совпадение, иначе False.
        """
        # Проверка на регулярные выражения
        if any(isinstance(locator, re.Pattern) for locator in locators):
            regexps = self._select_regexp(locators)
            if self._match_any(regexps, text_locator):
                return True

        # Проверка на точное совпадение
        return text_locator in locators

    def _select_regexp(self, locators):
        """
        Выбирает из списка локаторов только те, которые являются регулярными выражениями.

        :param locators: Список локаторов, который может содержать как строки, так и регулярные выражения.
        :return: Список регулярных выражений, найденных в локаторах.
        """
        return [locator for locator in locators if isinstance(locator, re.Pattern)]

    def _match_any(self, regexps, string):
        """
        Проверяет, совпадает ли строка с любым из переданных регулярных выражений.

        :param regexps: Список регулярных выражений.
        :param string: Строка для проверки.
        :return: True, если хотя бы одно регулярное выражение совпадает со строкой, иначе False.
        """
        return any(reg.match(string) for reg in regexps)

    def _load_page(self, key):
        """
        Загружает страницу по ключу, если она еще не была загружена.

        :param key: Ключ страницы, которая должна быть загружена.
        :return: Загруженная страница.
        """
        if key not in self.loaded_pages:
            self.loaded_pages[key] = self.loaders[key](self.driver)
        return self.loaded_pages[key]
