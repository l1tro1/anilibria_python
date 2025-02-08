from py_prism import PageSection, Sections, Elements
from selenium.webdriver.common.by import By

from features.support.page_object.sections.carousel_item_section import CarouselItemSection


class CarouselSection(PageSection):
    """
    Класс, представляющий секцию карусели на веб-странице. Наследуется от класса PageSection.

    Атрибуты:
        control_buttons_matcher (dict): Словарь, сопоставляющий названия кнопок управления с их CSS-классами.
        items (Sections): Элементы карусели, представляющие собой дочерние элементы класса CarouselItemSection.
        control_buttons (Elements): Элементы управления (кнопки "Назад" и "Вперед").

    Методы:
        control_button_by_name(name):
            Находит кнопку управления по названию (например, "Назад" или "Вперед") и возвращает соответствующий элемент.
    """
    control_buttons_matcher = {"Назад": 'mdi-chevron-left',
                               "Вперед": 'mdi-chevron-right'}

    items = Sections(CarouselItemSection,
                     By.XPATH,
                     ".//div[contains(@class,'v-carousel-item')]")
    control_buttons = Elements(By.XPATH, ".//div[contains(@class,'v-window__controls')]/button")

    def control_button_by_name(self, name: str):
        """
        Находит кнопку управления (например, "Назад" или "Вперед") по имени и возвращает соответствующий элемент.

        Параметры:
            name (str): Название кнопки управления. Может быть "Назад" или "Вперед".

        Возвращает:
            WebElement: Элемент кнопки управления, соответствующий переданному названию.

        Исключения:
            KeyError: Если передано имя, которое не содержится в словаре control_buttons_matcher.
        """
        button_class = self.control_buttons_matcher[name]
        for control_button in self.control_buttons:
            classes = control_button.get_attribute('class').split()
            if classes.include(button_class):
                return control_button
