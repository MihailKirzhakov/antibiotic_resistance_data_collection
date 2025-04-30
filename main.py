from params.config import settings, args

from utils.get_data_from_pdf import add_to_table
from utils.convert_word_to_pdf import convertation
from utils.gui import gui_app


def main(convert=False, add=False, gui=False):
    # Если передан аргумент -g, запускаем графический интерфейс
    if gui:
        gui_app.run()
        return

    # Если передан аргумент -c, выполняем только конвертирование
    if convert:
        convertation(settings.MAIN_FOLDER_PATH)
        return

    # Если передан аргумент -a, выполняем только сбор и упаковку данных
    if add:
        add_to_table(settings.MAIN_EXCEL_FILE_PATH)
        return

    # Если не переданы аргументы, выполняем оба действия последовательно
    convertation(settings.MAIN_FOLDER_PATH)
    add_to_table(settings.MAIN_EXCEL_FILE_PATH)


if __name__ == '__main__':

    # Запуск программы
    try:
        main(convert=args.convert, add=args.add, gui=args.gui)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
