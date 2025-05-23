# antibiotic_resistance_data_collection

Проект antibiotic_resistance_data_collection создан для автоматизации процесса выполнения мониторинга антибиотикорезистентности микроорганизмов!

## Что делает код?

- Программа конвертирует файлы формата .doc/.docx в формат PDF. (Это весьма костальное решение по причине того,
                                                               что данные в word файлах содержались во вложенных таблицах друг в друга,
                                                               поэтому было принято решение вывести все в формат PDF и спарсить оттуда текст)
- Далее программа собирает данные из текста, используя регулярные выражения и передаёт их в Pandas.
- После этого Pandas упаковывает данные и переносит их в готовую, заранее настроенную Excel таблицу.

В дальнейшим программа будет дорабатываться, будет подключен прямой способ получения данных из БД, а также Pandas будет использоваться по назначению
для обработки и получения статистических данных, а также визуализации данных в виде таблиц, графиков и прочее.

## Используемые технологии<a id="technologies-project"></a>:

![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-brightgreen?style=flat&logo=pandas)
![Pydantic](https://img.shields.io/badge/Pydantic-grey?style=flat)
![Customtkinter](https://img.shields.io/badge/Customtkinter-blue?style=flat)

## Как развернуть проект

1. Клонировать репозиторий, создать виртуальное окружение, установить зависимости:
```
git@github.com:MihailKirzhakov/antibiotic_resistance_data_collection.git
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
2. Заполнить файл .env
```
# Если вы будете использовать программу без графического интерфейса, то вам нужно
# указать ути к папкам/файлам, для корректной работы
MAIN_EXCEL_FILE_PATH=C:/ваш/путь/до/файла.xlsx
MAIN_FOLDER_PATH=C:/ваш/путь/до/папки/с/файлами
...
```
3. Запустить скрипт можно как с аргументами так и без:
  1) ```python main.py``` Запустит программу с графическим интерфейсом
  2) ```python main.py -c``` Запустит скрипт только для конвертирования
  3) ```python main.py -a``` Запустит скрипт только для сбора и переноса данных в файл Excel

## Автор проекта

**Михаил Киржаков** Email: kirzhakovma@mail.ru

[![Telegram](https://img.shields.io/badge/Telegram-blue?logo=telegram&logoColor=white)](https://t.me/Stoparrik)
[![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/MihailKirzhakov)
