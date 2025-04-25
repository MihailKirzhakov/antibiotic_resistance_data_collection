import os
import re

import pandas as pd
from pandas import DataFrame
import pdfplumber
from tqdm import tqdm

from params.antibiotics import antibiotic_list
from params.config import settings
from params.constants import (
    MAIN_SHEET_NAME, CULTURES, TITER, DEPARTMENT, CARD_NUMBER,
    STUDIED_BIOMATERIAL, DATE_TAKEN, DATE_COMPLETED,
    CULTURE_PATTERN, TITER_PATTERN, CARD_NUMBER_PATTENR,
    STUDIED_BIOMATERIAL_PATTERN, DATE_TAKEN_PATTERN,
    DATE_COMPLETED_PATTERN, COLLECTING_PROCESS,
    COLLECT_DATA_ERROR, COMPLETE_COLLECT_PACKAGE,
    ANALYSIS_SHEET_NAME, ATTENTION_NEW_BACTERIA
)
from params.departments import departments
from .exceptions import GetDataFromPdfError, SaveToExcelFileError
from .decorators import redirect_stderr_to_log


# Получение главного DataFrame из существующего файла
df: DataFrame = pd.read_excel(
    settings.MAIN_EXCEL_FILE_PATH,
    sheet_name=MAIN_SHEET_NAME, engine='openpyxl'
)

# Получение DataFrame с данными о имеющихся бактериях
bacteria_list_df: DataFrame = pd.read_excel(
    settings.MAIN_EXCEL_FILE_PATH,
    sheet_name=ANALYSIS_SHEET_NAME, engine='openpyxl'
)


def get_data_from_pdf(file_path: str) -> tuple:
    """Функция для сбора данных из файла PDF

    Основное применение - с помощью регулярных выражений осуществляет
    поиск конкретных данных в искомом файле формата PDF

    Для чтения файлов PDF используется библиотека 'pdfplumber'

    Args:
        file_path (str): Путь к файлу PDF

    Returns:
        tuple: Возвращает кортеж:
            - Список найденных культур в посеве
            cultures: list[str] = list()
            - Титры культур
            titer_list: list[str] = list()
            - Отделение
            department: str | None = None
            - Номер истории болезни
            card_number: str | None = None
            - Исследуемый биоматериал
            studied_biomaterial: str | None = None
            - Дата взятия биоматериала
            date_taken: str | None = None
            - Дата выполнения анализа
            date_completed: str | None = None
            - Словарь антибиотиков с резистентностью
            found_antibiotics: dict[str, list[str]] = dict()
    """

    try:
        # Открываем PDF файл
        with redirect_stderr_to_log(), pdfplumber.open(file_path) as pdf:

            cultures: list[str] = list()
            titer_list: list[str] = list()
            department: str | None = None
            card_number: str | None = None
            studied_biomaterial: str | None = None
            date_taken: str | None = None
            date_completed: str | None = None
            found_antibiotics: dict[str, list[str]] = dict()

            for page in pdf.pages:
                # Извлекаем текст
                text = page.extract_text()
                # Пакуем в таблицу значения резистентности
                tables = page.extract_tables()

                # Ищем культуры в посеве
                matches = re.findall(CULTURE_PATTERN, text)
                if matches:
                    for match in matches:
                        cultures.append(match)

                # Ищем титры
                titer_matches = re.findall(TITER_PATTERN, text)
                if titer_matches:
                    for number in titer_matches:
                        # Преобразуем в формат 10^n
                        titer_list.append(f'10^{len(number) - 1}')

                # Ищем отделение
                for key, value in departments.items():
                    if key:
                        department_match = re.search(re.escape(key), text)
                        if department_match:
                            department = value
                            break

                # Ищем номер карты
                card_number_match = re.search(CARD_NUMBER_PATTENR, text)
                if card_number_match:
                    card_number = card_number_match.group(1)

                # Ищем исследуемый биоматериал
                studied_biomaterial_match = re.search(
                    STUDIED_BIOMATERIAL_PATTERN, text
                )
                if studied_biomaterial_match:
                    studied_biomaterial = studied_biomaterial_match.group(1)

                # Ищем дату забора
                date_taken_match = re.search(DATE_TAKEN_PATTERN, text)
                if date_taken_match:
                    date_taken = date_taken_match.group(1)

                # Ищем дату выполнения
                date_completed_match = re.search(DATE_COMPLETED_PATTERN, text)
                if date_completed_match:
                    date_completed = date_completed_match.group(1)

                # Ищем результат резистентности
                for table in tables:
                    for row in table:
                        for row_value in row:
                            if row_value is not None:
                                antibiotic_pattern = r'\b(' + '|'.join(
                                    re.escape(antibiotic) for antibiotic
                                    in antibiotic_list
                                ) + r')\b(?=\s|\)|$)'
                                antibiotic_matches = re.findall(
                                    antibiotic_pattern, row_value
                                )
                                if antibiotic_matches:
                                    found_antibiotics[antibiotic_matches[0]] = row[1:]

        return (
            cultures, titer_list, department, card_number,
            studied_biomaterial, date_taken, date_completed,
            found_antibiotics
        )
    except GetDataFromPdfError as e:
        print(
            f'{COLLECT_DATA_ERROR} {file_path}: {e}'
        )
        return ([], [], None, None, None, None, None, {})


def add_to_table(output_file_path: str) -> DataFrame:
    """Функция для упаковки и передачи данных в файл excel

    Args:
        df (Class: DataFrame): Исходные данные, прочитанные из excel файла
        output_file_path (str): Путь к файлу excel,
                                в который будут записаны данные

    Returns:
        df (Class: DataFrame): Обновлённые данные
    """
    # Создаём словарь data, который будет упакован в новый DataFrame
    data: dict[str, list[str]] = {
        CULTURES: [],
        TITER: [],
        DEPARTMENT: [],
        CARD_NUMBER: [],
        STUDIED_BIOMATERIAL: [],
        DATE_TAKEN: [],
        DATE_COMPLETED: [],
    }

    # Создаём список имеющихся бактерий для сверки
    bacteria_list: list[str] = []
    new_bacteria_list: list[str] = []
    first_column_data = bacteria_list_df.iloc[:, 0]
    for name in first_column_data:
        bacteria_list.append(name)

    # Создаём столбцы с антибиотиками в словаре data
    for antibiotic in antibiotic_list:
        data[antibiotic] = []

    # Получаем список всех PDF файлов в указанной папке
    pdf_files = [
        filename for filename in os.listdir(settings.MAIN_FOLDER_PATH)
        if filename.endswith('.pdf')
    ]

    # Перебираем все файлы в указанной папке
    for filename in tqdm(pdf_files, desc=COLLECTING_PROCESS):
        if filename.endswith('.pdf'):
            file_path = os.path.join(settings.MAIN_FOLDER_PATH, filename)

        # Запускаем функцию по сбору данных из файла PDF
        # и распаковываем результат в переменные
        (
            cultures, titer_list, department, card_number,
            studied_biomaterial, date_taken, date_completed, found_antibiotics
        ) = get_data_from_pdf(file_path)

        # Выполняем процесс упаковки данных в новый DataFrame
        data[CULTURES].extend(cultures)
        data[TITER].extend(titer_list)
        for _ in cultures:
            data[DEPARTMENT].append(department)
            data[CARD_NUMBER].append(card_number)
            data[STUDIED_BIOMATERIAL].append(studied_biomaterial)
            data[DATE_TAKEN].append(date_taken)
            data[DATE_COMPLETED].append(date_completed)

        for found_antibiotic, resistance in found_antibiotics.items():
            data[found_antibiotic].extend(resistance)

        # Некий костыль для адекватной работы pandas.
        # Дозаполняем списки строк, для вставки данных без ошибок,
        # если высота столбца не совпадает, то добавляем пустую строку
        max_length = len(data[CULTURES])
        for key in data.keys():
            while len(data[key]) < max_length:
                data[key].append('')

    # Проверяем на наличие новых, не учтённых бактерий
    for value in data[CULTURES]:
        if value not in bacteria_list:
            new_bacteria_list.append(value)

    # Помещаем новые бактерии в текстовый файл,
    # если есть новые бактерии
    if len(new_bacteria_list) > 0:
        with open(os.path.join(os.getcwd(), 'new_bacteria.txt.'), 'w') as file:
            for bacteria in new_bacteria_list:
                file.write(f"{bacteria}\n")
        print(ATTENTION_NEW_BACTERIA)

    # Создаём обновлённый датафрейм
    new_df = pd.DataFrame(data)

    # Объединяем датафреймы
    concat_df = pd.concat([df, new_df])

    try:
        # Сохраняем в Excel
        with pd.ExcelWriter(
            output_file_path, mode='a',
            engine='openpyxl', if_sheet_exists='overlay'
        ) as writer:
            concat_df.to_excel(writer, index=False, sheet_name=MAIN_SHEET_NAME)
        print(COMPLETE_COLLECT_PACKAGE)
    except SaveToExcelFileError as e:
        print(
            f'Ошибка при сохранении данных в файл excel '
            f'{output_file_path}: {e}'
        )
