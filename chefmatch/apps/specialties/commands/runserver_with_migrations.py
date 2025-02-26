from django.core.management.commands.runserver import Command as RunserverCommand
from django.core.management import call_command
from django.db import connections
from django.db.migrations.executor import MigrationExecutor

class Command(RunserverCommand):
    def handle(self, *args, **options):
        print("Applying migrations...")
        call_command('migrate', interactive=False)

        super().handle(*args, **options)
