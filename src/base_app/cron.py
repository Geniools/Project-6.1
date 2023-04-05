import subprocess
import os

from datetime import datetime
from django_cron import CronJobBase, Schedule

from sports_accounting import settings


class MongoDBBackupJob(CronJobBase):
    # RUN_EVERY_MINS = 1440  # run every 24 hours
    RUN_EVERY_MINS = 1  # run every minute (for testing purposes)
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'base_app.mongodb_backup'
    
    def do(self):
        # define the name of the database to backup
        database_name = settings.MONGO_DB_DATABASE
        
        # define the Atlas connection string
        atlas_connection_string = settings.MONGO_DB_URI
        
        # define the directory where the backup should be stored
        backup_directory = settings.BASE_DIR / 'backup'
        
        if not backup_directory.exists():
            backup_directory.mkdir()
        
        # define the command to execute
        command = f'mongodump --uri="{atlas_connection_string}" --db="{database_name}" --out="{backup_directory.resolve()}"'
        
        # execute the command
        subprocess.run(command, shell=True)


class MySQLDBBackupJob(CronJobBase):
    # RUN_EVERY_MINS = 1440  # run every 24 hours
    RUN_EVERY_MINS = 1  # run every minute (for testing purposes)
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'base_app.mysql_backup'
    
    def do(self):
        database_name = settings.DATABASES['default']['NAME']
        # A user must have the right privileges to execute the command
        database_user = settings.DATABASES['default']['USER']
        database_password = settings.DATABASES['default']['PASSWORD']
        # ============================================================
        
        # define the directory where the backup should be stored
        backup_directory = settings.BASE_DIR / 'backup'
        backup_filename = f'{database_name}_diff_backup_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.sql'
        
        # Create backup command
        # command = f'mysqldump --user={database_user} --password={database_password} --databases {database_name} --skip-lock-tables --skip-add-drop-table > {backup_directory}/{backup_filename}'
        command = f'mysqldump --user="{database_user}" --password="{database_password}" --databases "{database_name}" > {os.path.join(backup_directory, backup_filename)}'
        
        # Execute backup command
        subprocess.run(command, shell=True)
        print(f'Differential backup for {database_name} created successfully: {backup_directory} / {backup_filename}')
