from py_prism import PageSection, Elements
from selenium.webdriver.common.by import By


class BreadcrumbsSection(PageSection):
    elements = Elements(By.XPATH, './a')

    def element_by_text(self, text):
        for element in self.elements:
            if element.text == text:
                return element
