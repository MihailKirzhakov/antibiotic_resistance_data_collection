import argparse

from params.config import settings
from params.constants import (
    MAIN_DESCRIPTION, CONVERT_DESCRIPTION, ADD_TO_TABLE_DESCRIPTION
)
from utils.get_data_from_pdf import add_to_table
from utils.convert_word_to_pdf import convertation


def main(convert=False, add=False):
    """Основная функция для запуска основной логики работы приложения.

    - При запуске приложения без аргументов, приложение выполнит ковертацию,
      затем выполнит сбор и упаковку данных последовательно.
    - Если запустить приложение с аргументом -c, то выполнится
      только конвертирование.
    - Если запустить приложение с аргументом -a, то выполнится
      только сбор и упаковка данных.
    """
    # Если передан аргумент -c, выполняем только конвертирование
    if convert or not (convert or add):
        convertation(settings.MAIN_FOLDER_PATH)

    # Если передан аргумент -a, выполняем только сбор и упаковку данных
    if add or not (convert or add):
        add_to_table(settings.MAIN_EXCEL_FILE_PATH)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=MAIN_DESCRIPTION
    )
    parser.add_argument(
        '-c', '--convert',
        action='store_true',
        help=CONVERT_DESCRIPTION
    )
    parser.add_argument(
        '-a', '--add',
        action='store_true',
        help=ADD_TO_TABLE_DESCRIPTION
    )

    args = parser.parse_args()
    try:
        main(convert=args.convert, add=args.add)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
