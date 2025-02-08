from selenium.webdriver.common.by import By

from py_prism import PageSection, Element


class DescriptionSection(PageSection):

    title = Element(By.XPATH, './a')

    body = Element(By.XPATH, "./div[contains(concat(' ', @class, ' '), ' ff-body ')]")
