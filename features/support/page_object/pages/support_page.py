from selenium.webdriver.common.by import By

from features.support.page_object.pages.root_page import Root
from features.support.page_object.sections import BreadcrumbsSection, DescriptionSection
from py_prism import Section


class Support(Root):
    _url = "https://anilibria.top/support"

    breadcrumbs = Section(BreadcrumbsSection,
                          By.XPATH,
                          "//div[contains(@class,'v-container')]/div/div[@class='d-flex align-baseline ff-heading text-unselect mb-2']")

    description = Section(DescriptionSection,
                          By.XPATH,
                          "//div[contains(@class,'text-unselect mb-4')]")
