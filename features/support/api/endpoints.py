import json
import re
from typing import Optional, List, Dict


class ElementCountError(Exception):
    pass


class Endpoints:
    def __init__(self, file_path: str = 'files/anilibria_api_endpoints.json'):
        """
        Инициализация класса Endpoints.

        Args:
             file_path: Путь к JSON-файлу с данными о конечных точках API.
        """
        self._endpoints = self._load_endpoints(file_path)

    def _load_endpoints(self, file_path: str) -> List[Dict]:
        """
        Загружает данные о конечных точках из JSON-файла.

        Args:
            file_path: Путь к JSON-файлу.
        Raises:
             FileNotFoundError: Если файл не найден
             json.JSONDecodeError: Если возникли ошибки парсинга Json
        Return:
             List[Dict]: Список конечных точек.
        """
        try:
            with open(file_path, encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file_path} не найден.")
        except json.JSONDecodeError:
            raise ValueError(f"Файл {file_path} имеет неверный формат JSON.")

    def find(self, description_part: str) -> Dict:
        """
        Находит одну конечную точку по части описания.

        Args:
            description_part (str): Часть описания для поиска.
        Raises:
            ElementCountError, если найдено более одного совпадения.
        Return:
             Dict: Информация о конечной точке.
        """
        results = self.find_all(description_part)
        if results is None:
            raise ElementCountError("Совпадений не найдено.")
        if len(results) > 1:
            raise ElementCountError("Среди API Endpoint найдено более одного совпадения.")
        return results[0]

    def find_all(self, description_part: str) -> Optional[List[Dict]]:
        """
        Находит все конечные точки, соответствующие части описания.

        Args:
            description_part (str): Часть описания для поиска.
        Return:
            Optional[List[Dict]]: Список найденных конечных точек или None, если совпадений нет.
        Raises:
            ValueError: Если параметр description_part пустой
        """
        if not description_part:
            raise ValueError("Параметр description_part не может быть пустым.")

        pattern = re.compile(f".*{re.escape(description_part)}.*", re.IGNORECASE)
        results = [info for info in self._endpoints if pattern.match(info.get('description', ''))]

        return results if results else None
