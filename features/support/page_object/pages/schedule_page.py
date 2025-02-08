from py_prism import Section, Element, Sections, Elements
from selenium.webdriver.common.by import By

from features.support.page_object.pages.root_page import Root
from features.support.page_object.sections import BreadcrumbsSection, CardSection, DescriptionSection, ListItemSection


class Schedule(Root):
    _url = "https://anilibria.top/anime/schedule"

    DICTIONARY = {
        'breadcrumbs': 'breadcrumbs',
        'описание': 'description',
        'поле поиска': 'search_field'
    }

    breadcrumbs = Section(BreadcrumbsSection, By.XPATH,
                          "//div[contains(@class,'v-container')]/div/div[@class='d-flex align-baseline ff-heading text-unselect mb-2']")

    description = Section(DescriptionSection,
                          By.XPATH,
                          "//div[contains(@class,'text-unselect mb-4')]")

    search_field = Element(By.XPATH,
                           "//main//input[contains(concat(' ', @class, ' '), ' v-field__input ')]")

    failed_search_result = Section(ListItemSection,
                                   By.XPATH,
                                   "//main//div[contains(concat(' ', @class, ' '), ' v-list-item ')]")

    success_search_results = Sections(ListItemSection, By.XPATH,
                                      "//main//a[contains(concat(' ', @class, ' '), ' v-list-item ')]")

    navs = Sections(CardSection, By.XPATH,
                    "//div[contains(concat(' ', @class, ' '), ' v-card ') and ./button]")

    posters = Elements(By.XPATH, "//div[contains(concat(' ', @class, ' '), ' v-row v-row--dense ')]/div")
    cards = Elements(By.XPATH, "//div[@class='masonry-wall']//div[@class='masonry-item']")

    def days(self):
        for card in self.navs:
            if card.columns[0].text == 'Все':
                return card

    def views(self):
        for card in self.navs:
            if card.columns[0].text == '':
                return card

    def day_by_name(self, name):
        for day in self.days().columns:
            if day.text == name:
                return day
