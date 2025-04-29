import os
import sys
from contextlib import contextmanager

from loguru import logger


@contextmanager
def redirect_stderr_to_log():
    """Контекстный менеджер для перенаправления stderr в лог с помощью loguru."""

    # Перенаправляем stderr в logger
    old_stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')

    try:
        yield
    except Exception as e:
        logger.error(f"Pdfplumber: {e}")
    finally:
        sys.stderr = old_stderr
