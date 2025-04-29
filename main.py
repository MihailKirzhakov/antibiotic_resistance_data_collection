from params.config import settings, args

from utils.get_data_from_pdf import add_to_table
from utils.convert_word_to_pdf import convertation


def main(convert=False, add=False):

    # Если передан аргумент -c, выполняем только конвертирование
    if convert or not (convert or add):
        convertation(settings.MAIN_FOLDER_PATH)

    # Если передан аргумент -a, выполняем только сбор и упаковку данных
    if add or not (convert or add):
        add_to_table(settings.MAIN_EXCEL_FILE_PATH)


if __name__ == '__main__':

    # Запуск программы
    try:
        main(convert=args.convert, add=args.add)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
