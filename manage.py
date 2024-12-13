#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.commands.runserver import Command as runserver

from BANK.wsgi import settings_module

# Встановлюємо порт за замовчуванням
runserver.default_port = "8080"

def main():
    """Run administrative tasks."""
    settings_module = 'BANK.deployment' if 'WEBSITE_HOST' in os.environ else 'BANK.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
