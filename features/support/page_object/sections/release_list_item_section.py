from py_prism import Element, PageSection
from selenium.webdriver.common.by import By


class ReleaseListItemSection(PageSection):

    title = Element(By.XPATH, ".//div[contains(concat(' ', @class, ' '), ' v-list-item__content ')]/div[1]")

    subtitle = Element(By.XPATH, ".//div[contains(concat(' ', @class, ' '), ' v-list-item__content ')]/div[2]")
