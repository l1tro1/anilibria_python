import pytest
import logging
from requests import Session
from unittest.mock import MagicMock, patch
from features.support.api.anilibria_rest import AnilibriaRest


# Фикстура для создания экземпляра AnilibriaRest
@pytest.fixture
def anilibria_rest():
    return AnilibriaRest()


# Тесты для класса AnilibriaRest
class TestAnilibriaRest:
    def test_initialization(self, anilibria_rest):
        """Проверка корректной инициализации класса."""
        assert anilibria_rest._url == "https://anilibria.top/api/v1"
        assert isinstance(anilibria_rest._session, Session)
        assert isinstance(anilibria_rest._logger, logging.Logger)

    def test_build_url(self, anilibria_rest):
        """Проверка создания полного URL."""
        endpoint = "/test"
        expected_url = "https://anilibria.top/api/v1/test"
        assert anilibria_rest._build_url(endpoint) == expected_url

    @patch("requests.Session.send")
    def test_request_success(self, mock_send, anilibria_rest):
        """Проверка успешного выполнения запроса."""
        # Настройка мок-ответа
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mock_send.return_value = mock_response

        # Вызов метода
        result = anilibria_rest._request("/test", alias_name="get")

        # Проверки
        assert result == {"key": "value"}
        mock_send.assert_called_once()

    def test_getattr_success(self, anilibria_rest):
        """Проверка динамического создания методов."""
        # Проверка доступных методов
        for method in anilibria_rest._AVAILABLE_METHODS:
            assert callable(getattr(anilibria_rest, method))

    def test_getattr_failure(self, anilibria_rest):
        """Проверка ошибки при вызове несуществующего метода."""
        with pytest.raises(AttributeError):
            anilibria_rest.invalid_method()

    @patch("requests.Session.send")
    def test_dynamic_methods(self, mock_send, anilibria_rest):
        """Проверка работы динамически созданных методов."""
        # Настройка мок-ответа
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mock_send.return_value = mock_response

        # Проверка каждого метода
        for method in anilibria_rest._AVAILABLE_METHODS:
            result = getattr(anilibria_rest, method)("/test")
            assert result == {"key": "value"}
            mock_send.assert_called_once()
            mock_send.reset_mock()
