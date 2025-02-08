from selenium.webdriver.common.by import By

from features.support.page_object.pages.root_page import Root
from py_prism import Section

from features.support.page_object.sections.carousel_section import CarouselSection


class Index(Root):
    _url = "https://anilibria.top/"

    carousel = Section(CarouselSection,
                       By.XPATH,
                       "//main//div[contains(concat(' ', @class, ' '), ' v-carousel ')]")
