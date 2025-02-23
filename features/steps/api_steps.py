import json

from behave import step
from jsonschema import validate
from features.support.api import AnilibriaRest, Endpoints


@step('получаю "{endpoint_description}" через rest')
def open_search_filter(context, endpoint_description):
    """
    Шаг для выполнения REST-запроса к указанному эндпоинту.

    Args:
        context: Контекст выполнения теста, содержащий информацию о текущем состоянии.
        endpoint_description (str): Описание эндпоинта, который нужно вызвать.

    Steps:
        1. Получает данные эндпоинта по его описанию из класса Endpoints.
        2. Выполняет REST-запрос с использованием метода и пути из данных эндпоинта.
        3. Сохраняет результат запроса и имя JSON-файла для схемы в контексте.

    Returns:
        None
    """
    endpoints = Endpoints()
    endpoint_data = endpoints.find(endpoint_description)
    rest = AnilibriaRest()
    context.logger.info(f"Выполняется запрос по пути {endpoint_data['path']}")
    result = getattr(rest, endpoint_data['method'])(endpoint_data['path'])
    json_name = endpoint_data['description'].replace(' ', '_').replace('.', '')
    rest_response = {"result": result,
                     "json_name": json_name}
    context.logger.info("Данные запроса успешно получены.")
    context.rest_response = rest_response


@step('валидирую схему данных, полученных через rest')
def validate_rest_response(context):
    """
    Шаг для валидации данных, полученных через REST-запрос, по JSON-схеме.

    Args:
        context: Контекст выполнения теста, содержащий информацию о текущем состоянии.

    Steps:
        1. Проверяет, что в контексте есть данные REST-запроса.
        2. Загружает JSON-схему из файла, соответствующего имени, сохраненному в контексте.
        3. Валидирует данные REST-запроса по загруженной схеме.

    Raises:
        AttributeError: Если контекст не содержит данных REST-запроса.
        jsonschema.exceptions.ValidationError: Если данные не соответствуют схеме.

    Returns:
        None
    """
    if not hasattr(context, 'rest_response'):
        raise AttributeError("Контекст не содержит данных из rest запроса по ключу rest_response.")
    rest_response = context.rest_response
    with open(f"features/files/types/{rest_response['json_name']}.json", encoding='utf-8') as file:
        schema = json.load(file)
    validate(rest_response['result'], schema)
    context.logger.info(f"Данные REST-запроса успешно валидированы по схеме '{rest_response['json_name']}.json'.")
