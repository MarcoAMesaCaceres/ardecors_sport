import os
from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Create a backup of the MySQL database and restore it if needed'

    def add_arguments(self, parser):
        parser.add_argument(
            '--restore',
            type=str,
            help='Restore the database from the specified backup file'
        )

    def handle(self, *args, **kwargs):
        if kwargs['restore']:
            self.restore_database(kwargs['restore'])
        else:
            self.backup_database()

    def backup_database(self):
        backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        os.makedirs(backup_dir, exist_ok=True)

        # Define the name of the backup file
        backup_file = os.path.join(
            backup_dir, f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
        )

        # Get database settings
        db_name = settings.DATABASES['default']['NAME']
        db_user = settings.DATABASES['default']['USER']
        db_password = settings.DATABASES['default']['PASSWORD']
        db_host = settings.DATABASES['default']['HOST']
        db_port = settings.DATABASES['default']['PORT']

        # Construct the mysqldump command
        dump_command = (
            f"mysqldump --user={db_user} --password={db_password} --host={db_host} --port={db_port} {db_name} > {backup_file}"
        )

        # Run the command to dump the database data to the backup file
        os.system(dump_command)

        self.stdout.write(self.style.SUCCESS(f'Successfully backed up the database to {backup_file}'))

    def restore_database(self, backup_file):
        # Get database settings
        db_name = settings.DATABASES['default']['NAME']
        db_user = settings.DATABASES['default']['USER']
        db_password = settings.DATABASES['default']['PASSWORD']
        db_host = settings.DATABASES['default']['HOST']
        db_port = settings.DATABASES['default']['PORT']

        # Construct the mysql command for restoring the database
        restore_command = (
            f"mysql --user={db_user} --password={db_password} --host={db_host} --port={db_port} {db_name} < {backup_file}"
        )

        # Run the command to restore the database from the backup file
        os.system(restore_command)

        self.stdout.write(self.style.SUCCESS(f'Successfully restored the database from {backup_file}'))