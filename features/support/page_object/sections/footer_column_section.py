from py_prism import PageSection, Element, Elements
from selenium.webdriver.common.by import By


class FooterColumnSection(PageSection):
    header = Element(By.XPATH,
                     "./div[contains(concat(' ', @class, ' '), ' v-list-subheader ')]")

    links = Elements(By.XPATH, ".//a")
