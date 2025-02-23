# Нужно для работы Monkeypatch'ей
import locale

import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from features.support.file_system.tmp import save_screenshot
from features.support.logger import logger
from features.support.page_object import matcher_loaders, matcher_pages, PageFactory
from behave.fixture import fixture, use_fixture_by_tag
# Нужно для работы Monkeypatch'ей
import features.support.monkeypatch.webdriver

# Нужно для корректной работы datetime.datetime.today().weekday()
locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")


def page_factory(context):
    russian_page_name = context.page_name
    return context.pf.page_at(russian_page_name)


@fixture
def register_chrome(context):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(10)
    context.pf = PageFactory(matcher_pages, matcher_loaders, context.driver)
    context.page_factory = page_factory
    context.logger.info(f"Версия webdriver:{webdriver.__version__}")


def before_all(context):
    context.logger = logger


fixture_registry = {
    "fixture.browser":   register_chrome
}


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)


def after_step(context, step):
    if step.status == "failed":
        context.logger.debug("Come to after_step failed")
        if hasattr(context, 'driver'):
            save_screenshot(context)


def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()
