from py_prism import PageSection, Element, Section
from selenium.webdriver.common.by import By

from features.support.page_object.sections.navigation_section import NavigationSection


class HeaderSection(PageSection):
    home_button = Element(By.XPATH,
                          './/a[@href="/"]')

    navigation = Section(NavigationSection, By.XPATH,
                         "./div[contains(@class, 'v-layout')]")

    random_release_button = Element(By.XPATH,
                                    "./button[.//i[contains(@class, 'mdi-filmstrip-box-multiple')]]")

    search_button = Element(By.XPATH,
                            "./button[.//i[contains(@class, 'mdi-magnify')]]")

    settings_button = Element(By.XPATH,
                              "./button[.//i[contains(@class, 'mdi-cog')]]")

    authorize_button = Element(By.XPATH,
                               "./a[.//i[contains(@class, 'mdi-account')]]")
