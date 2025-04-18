# Текстовые константы
SHEET_NAME = 'выгрузка'
CULTURES = 'Наименование микроорганизма'
TITER = 'Титр'
DEPARTMENT = 'Отделение'
CARD_NUMBER = '№ истории'
STUDIED_BIOMATERIAL = 'Материал'
DATE_TAKEN = 'Дата приема'
DATE_COMPLETED = 'Дата выдачи'
MAIN_DESCRIPTION = (
    'Этот скрипт обрабатывает файлы: выполняет конвертацию '
    'и добавляет данные в таблицу.'
)
CONVERT_DESCRIPTION = 'Запуск отдельного конвертирования файлов'
ADD_TO_TABLE_DESCRIPTION = 'Запуск отдельного процесса сбора и добавления данных в excel файл'

# Паттерны регулярных выражений
CULTURE_PATTERN = r'\d+\.\s+([A-Za-z]+\s+[a-z]+)\s+\d+\s+KOE/мл'
TITER_PATTERN = r'(\d+)\s+KOE'
CARD_NUMBER_PATTENR = r'Номер карты:\s*(\d+/\w+)'
STUDIED_BIOMATERIAL_PATTERN = r'Исследуемый биоматериал (.+)'
DATE_TAKEN_PATTERN = r'Дата забора:\s*(\d{2}.\d{2}.\d{4})'
DATE_COMPLETED_PATTERN = r'Дата выполнения:\s*(\d{2}.\d{2}.\d{2})'
ANTIBIOTIC_PATTERN_PART = r'\s*\((.*?)\)\s*([SIR])'
