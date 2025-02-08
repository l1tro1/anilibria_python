from selenium.webdriver.common.by import By

from py_prism import PageSection, Elements, Element


class CardSection(PageSection):

    columns = Elements(By.XPATH, "./button")

    poster = Element(By.XPATH, "./button[.//i[contains(@class,'mdi-filmstrip-box')]]")

    cards = Element(By.XPATH, "./button[.//i[contains(@class,'mdi-id-card')]]")
