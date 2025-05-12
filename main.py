from params.config import settings, args

from utils.get_data_from_pdf import add_to_table
from utils.convert_word_to_pdf import convertation
from utils.gui import gui_app


def main(convert=False, add=False):

    # Если передан аргумент -c, выполняем только конвертирование
    if convert:
        if not settings.MAIN_FOLDER_PATH:
            return print('В файле .env не указан путь до папки с файлами .doc/.docx')
        convertation(settings.MAIN_FOLDER_PATH)
        return

    # Если передан аргумент -a, выполняем только сбор и упаковку данных
    if add:
        if not settings.MAIN_EXCEL_FILE_PATH:
            return print('В файле .env не указан путь до файла .xlsx')
        add_to_table(settings.MAIN_EXCEL_FILE_PATH)
        return

    # Если не переданы аргументы, запускаем программу с графическим интерфейсом
    gui_app.run()


if __name__ == '__main__':

    # Запуск программы
    try:
        main(convert=args.convert, add=args.add)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
