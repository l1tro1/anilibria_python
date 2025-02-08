from py_prism import PageSection, Element, Elements
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class FilterPartSection(PageSection):
    """
    Модуль, определяющий секцию фильтра на странице с использованием библиотеки Selenium и py_prism.

    Этот модуль описывает класс `FilterPartSection`, который представляет собой часть страницы с фильтром.
    Класс использует методы из библиотеки py_prism для взаимодействия с элементами страницы.

    Класс:
        FilterPartSection: Секция фильтра с различными элементами, такими как заголовок, подзаголовок, кнопки и слайдеры.

    Атрибуты класса:
        title (Element): Элемент, представляющий заголовок фильтра. Находит элемент с помощью XPath,
         который ищет `div` с классом `ff-heading`.
        subtitle (Element): Элемент, представляющий подзаголовок фильтра. Находит элемент с помощью XPath,
         который ищет `div` с классом `ff-body`.
        buttons (Elements): Коллекция элементов, представляющая кнопки фильтра (с использованием класса `v-chip`).
         Находит все элементы с этим классом внутри секции.
        slider_start (Element): Элемент, представляющий начальную позицию слайдера. Находит элемент с помощью XPath,
         который ищет `input`, содержащий подстроку `_start` в id.
        slider_end (Element): Элемент, представляющий конечную позицию слайдера. Находит элемент с помощью XPath,
         который ищет `input`, содержащий подстроку `_stop` в id.

    Примечание:
        Все элементы являются обертками вокруг веб-элементов с использованием библиотеки `py_prism`, которая упрощает работу с DOM-элементами.
    """
    title = Element(By.XPATH, "./div[contains(@class, 'ff-heading')]")
    subtitle = Element(By.XPATH, "./div[contains(@class, 'ff-body')]")
    buttons = Elements(By.XPATH, ".//span[contains(@class, 'v-chip')]")
    slider_start = Element(By.XPATH, ".//div[contains(@class,'v-slider-thumb v-locale--is-ltr')][1]")
    slider_end = Element(By.XPATH, ".//div[contains(@class,'v-slider-thumb v-locale--is-ltr')][2]")
    slider = Element(By.XPATH, ".//div[@class='v-slider-track']")

    def button_by_name(self, button_name):
        for button in self.buttons:
            if button.text == button_name:
                return button

    def slide_to_range(self, slider_range):
        # Делю период
        period = list(map(int, slider_range.split('-')))
        action = ActionChains(self.driver)
        # Получаю границы мин/макс
        min_value = int(self.slider_start.get_attribute("aria-valuemin"))
        max_value = int(self.slider_end.get_attribute("aria-valuemax"))
        # Получаю размер слайдера
        width = self.slider.size['width']
        # Узнаю сколько пикселей в одном делении слайдера
        step_length = 1 / (max_value - min_value) * width
        # Понимаю сколько нужно сдвинуть пикселей чтобы получить начальный диапазон
        offset = (period[0] - min_value) * step_length
        action.click_and_hold(self.slider_start).move_by_offset(offset, 0).release().perform()
        self.title.click()
        # Понимаю сколько нужно сдвинуть пикселей чтобы получить конечный диапазон
        offset = (max_value - period[1]) * step_length - step_length
        action.click_and_hold(self.slider_end).move_by_offset(-offset, 0).release().perform()
