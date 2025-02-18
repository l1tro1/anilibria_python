import pytest
import re
from unittest.mock import MagicMock
from features.support.page_object.page_factory import PageFactory


# Фикстура для создания тестового драйвера
@pytest.fixture
def mock_driver():
    return MagicMock()


# Фикстура для создания тестового PageFactory
@pytest.fixture
def page_factory(mock_driver):
    pages = {
        "home": ["Home Page", re.compile(r"Welcome to .*")],
        "about": ["About Us", re.compile(r"About .*")],
        "contact": ["Contact Us"],
    }
    loaders = {
        "home": MagicMock(return_value="Home Page Loaded"),
        "about": MagicMock(return_value="About Page Loaded"),
        "contact": MagicMock(return_value="Contact Page Loaded"),
    }
    return PageFactory(pages, loaders, mock_driver)


class TestPageFactory:
    def test_initialization(self, page_factory):
        """Проверка корректной инициализации PageFactory."""
        assert page_factory.pages is not None
        assert page_factory.loaders is not None
        assert page_factory.loaded_pages == {}
        assert page_factory.driver is not None

    def test_page_at_exact_match(self, page_factory):
        """Проверка поиска страницы по точному совпадению."""
        result = page_factory.page_at("Home Page")
        assert result == "Home Page Loaded"

    def test_page_at_regexp_match(self, page_factory):
        """Проверка поиска страницы по регулярному выражению."""
        result = page_factory.page_at("Welcome to Our Site")
        assert result == "Home Page Loaded"

    def test_page_at_no_match(self, page_factory):
        """Проверка ошибки, если страница не найдена."""
        with pytest.raises(KeyError):
            page_factory.page_at("Non-existent Page")

    def test_matches_locator_exact_match(self, page_factory):
        """Проверка совпадения локатора по точному совпадению."""
        locators = ["Home Page", re.compile(r"Welcome to .*")]
        assert page_factory._matches_locator(locators, "Home Page") is True

    def test_matches_locator_regexp_match(self, page_factory):
        """Проверка совпадения локатора по регулярному выражению."""
        locators = ["Home Page", re.compile(r"Welcome to .*")]
        assert page_factory._matches_locator(locators, "Welcome to Our Site") is True

    def test_matches_locator_no_match(self, page_factory):
        """Проверка отсутствия совпадения локатора."""
        locators = ["Home Page", re.compile(r"Welcome to .*")]
        assert page_factory._matches_locator(locators, "About Us") is False

    def test_select_regexp(self, page_factory):
        """Проверка выбора регулярных выражений из списка локаторов."""
        locators = ["Home Page", re.compile(r"Welcome to .*"), "About Us"]
        regexps = page_factory._select_regexp(locators)
        assert len(regexps) == 1
        assert isinstance(regexps[0], re.Pattern)

    def test_match_any(self, page_factory):
        """Проверка совпадения строки с любым из регулярных выражений."""
        regexps = [re.compile(r"Welcome to .*"), re.compile(r"About .*")]
        assert page_factory._match_any(regexps, "Welcome to Our Site") is True
        assert page_factory._match_any(regexps, "About Us") is True
        assert page_factory._match_any(regexps, "Contact Us") is False

    def test_load_page(self, page_factory):
        """Проверка загрузки страницы."""
        result = page_factory._load_page("home")
        assert result == "Home Page Loaded"
        assert "home" in page_factory.loaded_pages

    def test_load_page_cached(self, page_factory):
        """Проверка кэширования загруженных страниц."""
        page_factory._load_page("home")
        page_factory._load_page("home")
        page_factory.loaders["home"].assert_called_once()
