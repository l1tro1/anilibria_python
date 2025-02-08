from py_prism import PageSection, Elements
from selenium.webdriver.common.by import By


class NavigationSection(PageSection):

    buttons = Elements(By.XPATH, ".//a")

    def button_by_name(self, button_name):
        for button in self.buttons:

            if button.text == button_name:
                return button
