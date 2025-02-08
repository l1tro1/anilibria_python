import time
from http.cookiejar import LoadError
from selenium.webdriver.common.by import By

from features.support.page_object.sections.footer_section import FooterSection
from py_prism import Page, Element, Section
from features.support.page_object.sections.header_section import HeaderSection
from features.support.logger import logger


class Root(Page):

    nuxt_indicator = Element(By.XPATH, "//div[@class='nuxt-loading-indicator']")
    header = Section(HeaderSection, By.XPATH,
                     "//header//div[contains(@class, 'v-container')]/div[contains(@class, 'v-layout')]")

    footer = Section(FooterSection, By.XPATH, "//footer/div")

    def wait_load(self):
        start_time = int(time.time())
        start_time2 = int(time.time())
        nuxt_loaded = self.has_nuxt_indicator()
        while not nuxt_loaded:
            nuxt_loaded = self.has_nuxt_indicator()
            if int(time.time()) - start_time >= 10:
                raise LoadError("Страница не успела загрузиться за 10 секунд")
        time.sleep(2)
        logger.info(f"Время загрузки страницы {self.__class__.__name__} - {int(time.time()) - start_time2} секунд")
        return True
