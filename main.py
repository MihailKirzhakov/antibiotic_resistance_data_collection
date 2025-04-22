import argparse

from params.config import settings
from params.constants import (
    MAIN_DESCRIPTION, CONVERT_DESCRIPTION, ADD_TO_TABLE_DESCRIPTION,
    COMPLETE_CONVERSION, COMPLETE_COLLECT_TRANSFER
)
from utils.get_data_from_pdf import df, add_to_table
from utils.convert_word_to_pdf import convertation


def main(convert=False, add=False):
    if convert or not (convert or add):
        convertation(settings.MAIN_FOLDER_PATH)
        print(COMPLETE_CONVERSION)

    if add or not (convert or add):
        add_to_table(df, settings.MAIN_EXCEL_FILE_PATH)
        print(COMPLETE_COLLECT_TRANSFER)


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
