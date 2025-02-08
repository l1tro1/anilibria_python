from selenium.webdriver.common.by import By
from py_prism import PageSection, Element


class SearchFilterButtonSection(PageSection):
    """
    Класс для взаимодействия с разделом кнопки фильтра в пользовательском интерфейсе.

    Наследуется от PageSection и предназначен для управления состоянием кнопки фильтра на странице.
    """

    icon = Element(By.XPATH, './/i')
    """
    Элемент, представляющий иконку фильтра.
    Иконка используется для определения состояния фильтра (открыт/закрыт).
    """

    def _is_filter_opened(self) -> bool:
        """
        Проверяет, открыт ли фильтр.

        :return: bool - True, если фильтр закрыт (иконка имеет класс 'mdi-filter-off'),
                  иначе False.
        """
        return 'mdi-filter-off' in self.icon.get_attribute('class').split()

    def open(self) -> None:
        """
        Открывает фильтр, если он ещё не открыт.

        Если фильтр уже открыт, метод ничего не делает.
        """
        if not self._is_filter_opened():
            self.base_element.click()

    def close(self) -> None:
        """
        Закрывает фильтр, если он ещё не закрыт.

        Если фильтр уже закрыт, метод ничего не делает.
        """
        if self._is_filter_opened():
            self.base_element.click()
