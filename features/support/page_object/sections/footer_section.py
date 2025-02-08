from selenium.webdriver.common.by import By

from features.support.page_object.sections.footer_column_section import FooterColumnSection
from py_prism import PageSection, Sections


class FooterSection(PageSection):
    """
       Класс, представляющий секцию нижнего колонтитула страницы (Footer).

       Наследуется от базового класса PageSection и содержит функционал
       для работы со списком колонок в нижнем колонтитуле страницы.
    """

    columns = Sections(FooterColumnSection,
                       By.XPATH,
                       "./div[./div[contains(concat(' ', @class, ' '), ' v-list-subheader ')]]")
    """
    Переменная для поиска и хранения списка колонок в нижнем колонтитуле.

    Используется с помощью XPath, чтобы найти дочерние элементы div,
    содержащие классы с подстрокой 'v-list-subheader'.
    """

    def column_by_header(self, header_name: str):
        """
        Метод для поиска колонки по её заголовку.

        :param header_name: Название заголовка колонки, которое нужно найти.
        :type header_name: str
        :return: Объект колонки, соответствующий заголовку, если найден.
        :rtype: FooterColumnSection или None
        """
        for column in self.columns:
            if column.text == header_name:
                return column
