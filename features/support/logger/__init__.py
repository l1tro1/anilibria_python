import logging

from selenium.common import NoSuchElementException


# Кастомный форматтер для цветной подсветки
class ColoredFormatter(logging.Formatter):

    COLORS = {
        "RESET": "\033[0m",
        "INFO": "\033[34m",   # Зелёный
        "WARNING": "\033[33m",  # Жёлтый
        "ERROR": "\033[31m",  # Красный
        "DEBUG": "\033[37m",  # Синий
        "CRITICAL": "\033[1;31m"  # Жирный красный
    }

    def format(self, record):

        color = self.COLORS.get(record.levelname, "")
        reset = self.COLORS.get("RESET")
        base_message = super().format(record)
        return f"{color}{base_message}{reset}\r"


# Настройка логгера
logger = logging.getLogger("custom_logger")
logger.setLevel(logging.DEBUG)

# Создаём консольный обработчик
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Создаём и применяем форматтер с цветами
formatter = ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Добавляем обработчик логгера
logger.addHandler(console_handler)


def check_element(element, part):
    if element is None:
        message = f"На странице нет элемента {part} "\
                  "или он не описан в PageObject"
        raise NoSuchElementException(message)
