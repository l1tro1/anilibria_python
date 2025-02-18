import pytest
import json
from features.support.api.endpoints import Endpoints, ElementCountError


@pytest.fixture
def temp_json_file(tmp_path):
    data = [
        {"description": "API для авторизации пользователей",
         "path": "/auth"},
        {"description": "API для получения данных о пользователях",
         "path": "/users"},
        {"description": "API для управления товарами",
         "path": "/products"},
    ]
    file_path = tmp_path / "test_endpoints.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)
    return file_path


class TestEndpoints:

    def test_load_endpoints_success(self, temp_json_file):
        """Проверка успешной загрузки данных из JSON-файла."""
        endpoints = Endpoints(temp_json_file)
        assert len(endpoints._endpoints) == 3

    def test_load_endpoints_file_not_found(self):
        """Проверка обработки ошибки, если файл не найден."""
        with pytest.raises(FileNotFoundError):
            Endpoints("non_existent_file.json")

    def test_load_endpoints_invalid_json(self, tmp_path):
        """Проверка обработки ошибки, если файл имеет неверный формат JSON."""
        invalid_json_file = tmp_path / "invalid.json"
        invalid_json_file.write_text("invalid json")
        with pytest.raises(ValueError):
            Endpoints(invalid_json_file)

    def test_find_success(self, temp_json_file):
        """Проверка успешного поиска одной конечной точки."""
        endpoints = Endpoints(temp_json_file)
        result = endpoints.find("авторизации")
        assert result["path"] == "/auth"

    def test_find_multiple_matches(self, temp_json_file):
        """Проверка ошибки, если найдено более одного совпадения."""
        endpoints = Endpoints(temp_json_file)
        with pytest.raises(ElementCountError):
            endpoints.find("API")

    def test_find_no_matches(self, temp_json_file):
        """Проверка ошибки, если совпадений не найдено."""
        endpoints = Endpoints(temp_json_file)
        with pytest.raises(ElementCountError):
            endpoints.find("несуществующий текст")

    def test_find_all_success(self, temp_json_file):
        """Проверка успешного поиска всех конечных точек."""
        endpoints = Endpoints(temp_json_file)
        results = endpoints.find_all("API")
        assert len(results) == 3

    def test_find_all_no_matches(self, temp_json_file):
        """Проверка возврата None, если совпадений нет."""
        endpoints = Endpoints(temp_json_file)
        results = endpoints.find_all("несуществующий текст")
        assert results is None

    def test_find_all_empty_description_part(self, temp_json_file):
        """Проверка ошибки, если description_part пустой."""
        endpoints = Endpoints(temp_json_file)
        with pytest.raises(ValueError):
            endpoints.find_all("")