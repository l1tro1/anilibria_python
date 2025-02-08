from py_prism import PageSection, Element
from selenium.webdriver.common.by import By


class CarouselItemSection(PageSection):
    content = Element(By.XPATH,
                      ".//div[contains(@class,'v-responsive__content')]")
