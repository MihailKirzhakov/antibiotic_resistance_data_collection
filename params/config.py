import argparse
from typing import Optional

from loguru import logger
from params.constants import (
    MAIN_DESCRIPTION, CONVERT_DESCRIPTION, ADD_TO_TABLE_DESCRIPTION,
    START_GUI
)
from pydantic_settings import BaseSettings

# -----------------------------------------------------------------
# Настраиваем лог обработчик
logger.remove()
logger.add(
    sink='log_info.log', level="INFO", rotation='5 MB', mode='a'
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

# Режим запуска GUI
parser.add_argument(
    '-g', '--gui',
    action='store_true',
    help=START_GUI
)

args = parser.parse_args()


# -----------------------------------------------------------------
# Настройки для получения переменных окружения из файла .env
class Settings(BaseSettings):
    MAIN_EXCEL_FILE_PATH: Optional[str]
    MAIN_FOLDER_PATH: Optional[str]
    DIABETIC_FOOT: str
    DIABETIC_KIDNEY_DISEASE: str
    NEUROENDOCRINOLOGY: str
    ENDOCRINOPATHIES_THERAPY: str
    PATHOLOGY_OF_PARATHYROID_GLANDS: str
    ANESTHESIOLOGY_AND_RESUSCITATION_CENTER: str
    CARDIOLOGY_AND_VASCULAR_SURGERY: str
    ENDOCRINOPATHIES_OF_EARLY_AGE: str
    ANDROLOGY_AND_UROLOGY: str
    DIABETES_FORECASTING_AND_INNOVATION: str
    SURGERY: str
    ASSISTED_REPRODUCTIVE_TECHNOLOGIES: str
    THYROID_GLAND: str
    CHILDHOOD_ENDOCRINE_TUMORS: str
    PEDIATRIC_SURGERY: str
    CHILDHOOD_DIABETES_MELLITUS: str
    OSTEOPOROSIS_AND_OSTEOPATHY: str
    PEDIATRIC_THYROIDOLOGY: str

    class Config:
        env_file = '.env'


settings = Settings()
