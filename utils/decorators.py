import os
import sys
from contextlib import contextmanager


@contextmanager
def redirect_stderr_to_log():
    """Контекстный менеджер для перенаправления stderr в файл логов."""
    log_file_path = os.path.join(os.getcwd(), 'log_info.txt')

    # Проверка размера файла и перезапись, если он превышает 1кб
    if os.path.exists(log_file_path) and os.path.getsize(log_file_path) > 8000:
        with open(log_file_path, 'w') as log_file:
            pass

    with open(log_file_path, 'a') as log_file:
        old_stderr = sys.stderr
        sys.stderr = log_file
        try:
            yield
        finally:
            sys.stderr = old_stderr
