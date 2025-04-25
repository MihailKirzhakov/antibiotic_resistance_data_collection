# Текстовые константы
MAIN_SHEET_NAME = 'выгрузка'
ANALYSIS_SHEET_NAME = 'анализ сводки'
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
ADD_TO_TABLE_DESCRIPTION = (
    'Запуск отдельного процесса сбора и добавления данных в excel файл'
)
COMPLETE_CONVERSION = 'Конвертирование завершено!'
COMPLETE_COLLECT_PACKAGE = 'Сбор и упаковка данных завершены!'
COLLECTING_PROCESS = 'Процесс сбора данных...'
COLLECT_DATA_ERROR = 'Ошибка при сборе данных из файла'
CHECK_PDF_FILES_ERROR = (
    'Для корректной работы программы необходимо удалить/убрать все '
    '.pdf файлы из папки'
)
ATTENTION_NEW_BACTERIA = (
    'Обратите внимание! Появились неучтённые бактерии! '
    'Их названия были внесены в файл new_bacteria.txt.'
)

# Паттерны регулярных выражений
CULTURE_PATTERN = r'\d+\.\s+([A-Za-z]+\s+[a-z]+)\s+\d+\s+KOE/мл'
TITER_PATTERN = r'(\d+)\s+KOE'
CARD_NUMBER_PATTENR = r'Номер карты:\s*(\d+/\w+)'
STUDIED_BIOMATERIAL_PATTERN = r'Исследуемый биоматериал (.+)'
DATE_TAKEN_PATTERN = r'Дата забора:\s*(\d{2}.\d{2}.\d{4})'
DATE_COMPLETED_PATTERN = r'Дата выполнения:\s*(\d{2}.\d{2}.\d{2})'
