from py_prism import PageSection, Element
from selenium.webdriver.common.by import By


class ListItemSection(PageSection):

    icon = Element(By.XPATH, "./div[@class='v-list-item__prepend']/i")

    title = Element(By.XPATH, ".//div[contains(concat(' ', @class, ' '), ' v-list-item-title ')]")

    subtitle = Element(By.XPATH, ".//div[contains(concat(' ', @class, ' '), ' v-list-item-subtitle ')]")
