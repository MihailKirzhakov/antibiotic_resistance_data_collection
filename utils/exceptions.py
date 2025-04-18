class GetDataFromPdfError(Exception):
    """Ошибка при открытии файла PDF"""
    pass


class SaveToExcelFileError(Exception):
    """Ошибка при сохранении файла Excel"""
    pass


class ConvertToPdfFileError(Exception):
    """Ошибка при конвертировании файла в PDF"""
    pass
