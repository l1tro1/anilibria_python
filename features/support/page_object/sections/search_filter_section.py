from selenium.webdriver.common.by import By
from features.support.page_object.sections import FilterSection
from py_prism import PageSection, Section, Elements


class SearchFilterSection(PageSection):
    """Класс для работы с секцией фильтров поиска."""

    # Секция фильтров
    filters = Section(FilterSection, By.XPATH, './div[1]')

    buttons = Elements(By.XPATH, './div[2]//button')

    def button_by_name(self, button_name):
        for button in self.buttons:
            if button.text == button_name:
                return button
