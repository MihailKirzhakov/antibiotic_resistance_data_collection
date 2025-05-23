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
CONVERTION_PROCESS = 'Процесс конвертирования'
COLLECT_DATA_ERROR = 'Ошибка при сборе данных из файла'
CHECK_PDF_FILES_ERROR = (
    'Для корректной работы программы необходимо удалить/убрать все '
    '.pdf файлы из папки'
)
PDF_FILE_EXISTS_ERROR = 'В папке нет .pdf файлов!'
ATTENTION_NEW_BACTERIA = (
    'Обратите внимание! Появились неучтённые бактерии! '
    'Их названия были внесены в файл ARDC_info.log.'
)
PD_ENGINE = 'openpyxl'
START_GUI = (
    'Запуск программы с графическим интерфейсом'
)
PROCESSING = 'Выполняю, пожалуйста подождите...'
CHOOSE_FILE = 'Выберите основной Excel файл'
CHOOSE_FOLDER = 'Выберите папку'
TO_CONVERT = 'Конвертировать'
TO_COLLECT_PACK = 'Обработать и упаковать данные'
CHOOSE_FILE_ERROR = 'Файл не выбран!'
CHOOSE_FOLDER_ERROR = 'Папка не выбрана!'
WARNING = 'Предупреждение'
NOTIFICATION = 'Оповещение!'
FINISHED_PROCESS = 'Процесс завершён'
ERROR = 'Ошибка!'
INSTRUCTION = 'Инструкция по использованию программы'
INSTRUCTION_TEXT = (
    '1. Необходимо выбрать путь к основному файлу .excel, куда будут '
    'помещаться результаты резистентности. По умолчанию таким файлом является '
    'resistance.xlsx, он уже заранее настроен\n\n'
    '2. Необходимо выбрать путь к папке, где храняться файлы .doc/.docx, '
    'для конвертирования в формат .pdf. '
    'В эту же папку будут помещены сконвертированные файлы .pdf\n\n'
    '3. Перед конвертированием файлов, убедитесь, что в папке нет файлов .pdf\n\n'
)
CREATE_BY = 'Разработчик: Михаил Киржаков\nEmail: kirzhakovma@mail.ru'
VERSION = '\nВерсия: 1.0.0'

# Паттерны регулярных выражений
CULTURE_PATTERN = r'\d+\.\s+([A-Za-z]+\s+[a-z]+)(?:\s+\d+\s+KOE/мл|\s*)?'
TITER_PATTERN = r'(\d+)\s+KOE'
CARD_NUMBER_PATTENR = r'Номер карты:\s*(\d+/\w+)'
STUDIED_BIOMATERIAL_PATTERN = r'Исследуемый биоматериал (.+)'
DATE_TAKEN_PATTERN = r'Дата забора:\s*(\d{2}.\d{2}.\d{4})'
DATE_COMPLETED_PATTERN = r'Дата выполнения:\s*(\d{2}.\d{2}.\d{2})'
