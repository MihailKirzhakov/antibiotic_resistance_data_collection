import argparse
from typing import Optional

from loguru import logger
from params.constants import (
    MAIN_DESCRIPTION, CONVERT_DESCRIPTION, ADD_TO_TABLE_DESCRIPTION
)
from pydantic_settings import BaseSettings

# -----------------------------------------------------------------
# Настраиваем лог обработчик
logger.remove()
logger.add(
    sink='ARDC_info.log', level="INFO", rotation='5 MB', mode='a'
)

# -----------------------------------------------------------------
# Добавляем возможность запуска программы с аргументами
# для работы в разных режимах
parser = argparse.ArgumentParser(
        description=MAIN_DESCRIPTION
    )

# Режим конвертирования
parser.add_argument(
    '-c', '--convert',
    action='store_true',
    help=CONVERT_DESCRIPTION
)

# Режим обработки и упаковки данных
parser.add_argument(
    '-a', '--add',
    action='store_true',
    help=ADD_TO_TABLE_DESCRIPTION
)

args = parser.parse_args()


# -----------------------------------------------------------------
# Настройки для получения переменных окружения из файла .env
class Settings(BaseSettings):
    MAIN_EXCEL_FILE_PATH: Optional[str] = None
    MAIN_FOLDER_PATH: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
