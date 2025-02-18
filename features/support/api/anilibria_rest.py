import logging
from requests import Request, Session
from requests.exceptions import RequestException


class AnilibriaRest:
    """
    Класс для выполнения HTTP-запросов к API Anilibria.

    Поддерживаемые методы: GET, POST, PUT, DELETE.
    """

    _AVAILABLE_METHODS = ['get', 'post', 'put', 'delete']

    def __init__(self):
        """
         Инициализация класса.

         Создает сессию и устанавливает базовый URL для API.
         """
        self._url = 'https://anilibria.top/api/v1'
        self._session = Session()
        self._logger = logging.getLogger(__name__)

    def _request(self, url, payload=None, alias_name=None):
        """
        Внутренний метод для выполнения HTTP-запроса.

        Args:
            url (str): Конечная точка API.
            payload (dict, optional): Данные для отправки в теле запроса.
            alias_name (str, optional): Имя HTTP-метода (например, 'get', 'post').

        Raises:
            RequestException: Если произошла ошибка при выполнении запроса.

        Returns:
            dict: Ответ от сервера в формате JSON.
        """
        try:
            request = Request(
                alias_name.upper(),
                self._build_url(url),
                data=payload,
                headers={'Content-Type': 'application/json'}
            )
            prepped = request.prepare()
            response = self._session.send(prepped, timeout=120)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            self._logger.error(f"Ошибка при выполнении запроса {alias_name.upper()} к {self._build_url(url)}: {e}")
            raise

    def __getattr__(self, name):
        """
        Перехват вызова несуществующих атрибутов для динамического создания методов.

        Args:
            name (str): Имя атрибута (HTTP-метода).

        Returns:
            function: Метод для выполнения HTTP-запроса.

        Raises:
            AttributeError: Если имя атрибута не поддерживается.
        """
        if name not in self._AVAILABLE_METHODS:
            message = f'"{self.__class__.__name__}" object has no attribute "{name}"'
            self._logger.error(message)
            raise AttributeError(message)

        def _method_missing(*args, **kwargs):
            return self._request(*args, alias_name=name, **kwargs)
        return _method_missing

    def _build_url(self, endpoint):
        """
        Создает полный URL для запроса.

        Args:
            endpoint (str): Конечная точка API.

        Returns:
            str: Полный URL.
        """
        return self._url + endpoint
