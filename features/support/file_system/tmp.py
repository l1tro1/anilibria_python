import os
import datetime
from features.support.logger import logger


def create_tmp():
    dir_path = "features/tmp"
    create_dir(dir_path)


def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        logger.debug(f"Директория {dir_path} успешно создана!")
    else:
        logger.info(f"Директория {dir_path} уже существует!")


def save_screenshot(context):
    name = context.scenario.name
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.strftime("%Y-%m-%d_%H:%M:%S")
    dir_path = f"features/tmp/{current_date}/{name}"
    create_dir(dir_path)
    screen_path = f"{dir_path}/{name}.png"
    context.driver.save_screenshot(screen_path)
