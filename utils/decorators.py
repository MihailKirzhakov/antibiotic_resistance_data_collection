import os
import sys
from contextlib import contextmanager


@contextmanager
def redirect_stderr_to_log():
    """Контекстный менеджер для перенаправления stderr в файл логов."""
    with open(os.path.join(os.getcwd(), 'log_info.txt'), 'w') as log_file:
        old_stderr = sys.stderr
        sys.stderr = log_file
        try:
            yield
        finally:
            sys.stderr = old_stderr
