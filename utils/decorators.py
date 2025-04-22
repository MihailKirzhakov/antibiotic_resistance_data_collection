import os
import sys
from contextlib import contextmanager


# Устанавливаем путь и название лог файла, он будет сохраняться
# в папке с исполняемым файлом
log_file_path = os.path.join(os.getcwd(), 'log_info.txt')


@contextmanager
def redirect_stderr_to_log():
    """Контекстный менеджер для перенаправления stderr в файл логов."""
    with open(log_file_path, 'a') as log_file:
        old_stderr = sys.stderr
        sys.stderr = log_file
        try:
            yield
        finally:
            sys.stderr = old_stderr
