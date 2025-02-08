from selenium.webdriver.common.by import By

from features.support.page_object.sections import FilterPartSection
from py_prism import PageSection, Sections


class FilterSection(PageSection):
    parts = Sections(FilterPartSection,
                     By.XPATH,
                     "./div[contains(concat(' ', @class, ' '), ' v-card ')]")

    def part_by_title(self, title):
        for part in self.parts:
            if part.title.text == title:
                return part
