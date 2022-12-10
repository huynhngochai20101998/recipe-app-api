"""
Django command to wait for the databases to be available.
"""
import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg20Error


class Command(BaseCommand):
    """Django command to wait for the databases"""

    def handle(self, error=Psycopg20Error, *args, **kwargs):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
