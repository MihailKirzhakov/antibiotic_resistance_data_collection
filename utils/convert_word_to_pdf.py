import os

from docx2pdf import convert

from utils.exceptions import ConvertToPdfFileError
from params.constants import CHECK_PDF_FILES_ERROR, COMPLETE_CONVERSION


def convertation(work_folder: str) -> None:
    """
    Функция конвертирует файлы формата .docx в формат .pdf в ту же папку,
    используя библиотеку 'docx2pdf'

    Args:
        work_folder (str): Путь к папке с файлами .docx/.doc

    Returns:
        None
    """

    files_in_folder = os.listdir(work_folder)

    # Упаковываем в список файлы, которые будем конвертировать,
    # отбирая их по формату .docx
    pdf_files = [filename for filename in files_in_folder if filename.endswith('.pdf')]
    if pdf_files:
        return print(f'{CHECK_PDF_FILES_ERROR} {work_folder}')
    else:
        # Получаем список файлов .docx и .doc
        word_files = [
            filename for filename in files_in_folder
            if filename.endswith('.docx') or filename.endswith('.doc')
        ]

    # Перебираем список
    for index, input_file in enumerate(word_files, start=1):
        input_path = os.path.join(work_folder, input_file)
        output_file = os.path.join(work_folder, f'Posev{index}.pdf')

        try:
            # Конвертация
            convert(input_path, output_file)
        except ConvertToPdfFileError as e:
            print(f'Ошибка при конвертации файла {input_file}: {e}')

    print(COMPLETE_CONVERSION)
