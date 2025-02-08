from selenium.webdriver.common.by import By

from py_prism import PageSection, Element, Elements


class FooterColumnSection(PageSection):
    header = Element(By.XPATH,
                     "./div[contains(concat(' ', @class, ' '), ' v-list-subheader ')]")

    links = Elements(By.XPATH, ".//a")
