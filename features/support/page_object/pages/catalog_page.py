from selenium.webdriver.common.by import By

from features.support.page_object.pages.root_page import Root
from features.support.page_object.sections import (BreadcrumbsSection, DescriptionSection,
                                                   ListItemSection, ReleaseListItemSection,
                                                   SearchFilterButtonSection, SearchFilterSection)
from py_prism import Section, Element, Sections


class Catalog(Root):
    _url = "https://anilibria.top/anime/catalog"
    _input_xpath = "//input[contains(concat(' ', @class, ' '), ' v-field__input ')]"

    breadcrumbs = Section(BreadcrumbsSection, By.XPATH,
                          "//div[contains(@class,'v-container')]/div/div[@class='d-flex align-baseline ff-heading text-unselect mb-2']")

    description = Section(DescriptionSection,
                          By.XPATH,
                          "//div[contains(@class,'text-unselect mb-4')]")

    search_field = Element(By.XPATH,
                           f"//main{_input_xpath}")

    failed_search_result = Section(ListItemSection,
                                   By.XPATH,
                                   "//main//div[contains(concat(' ', @class, ' '), ' v-list-item ')]")

    success_search_results = Sections(ReleaseListItemSection, By.XPATH,
                                      "//main//a[contains(concat(' ', @class, ' '), ' v-list-item ')]")

    search_filter_button = Section(SearchFilterButtonSection, By.XPATH,
                                   f"//main//button[./preceding-sibling::div[.{_input_xpath}]]")
    search_filter = Section(SearchFilterSection, By.XPATH, "//div[@class='sticky-scrollbar-container']")
