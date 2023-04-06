import os
import subprocess

from datetime import datetime
from django_cron import CronJobBase, Schedule

from sports_accounting import settings


class MongoDBBackupJob(CronJobBase):
    # Example of how to run a job at different times
    # RUN_WEEKLY_ON_DAYS = [0] # run every Monday
    # RUN_MONTHLY_ON_DAYS = [1, 10] # run on the 1st and 10th of every month
    # RUN_AT_TIMES = ["11:00", "12:30"] # run at 11:00 and 12:30
    # ======================================================================
    # RUN_EVERY_MINS = 1440  # run every 24 hours
    RUN_EVERY_MINS = 1  # run every minute (for testing purposes)
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'mongodb_backup'
    
    def do(self):
        """
        Will create a backup of the MongoDB database
        Requires to have the 'mongodump' command installed on the system
        :return:
        """
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
        print(f'Full MongoDB backup for {database_name} created in: {backup_directory.resolve()}')


class MySQLDBBackupJob(CronJobBase):
    # RUN_EVERY_MINS = 1440  # run every 24 hours
    RUN_EVERY_MINS = 1  # run every minute (for testing purposes)
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'mysql_backup'
    
    def do(self):
        """
        Will create a backup of the MySQL database
        Requires to have the 'mysqldump' command installed on the system
        :return:
        """
        database_name = settings.DATABASES['default']['NAME']
        # A user must have the right privileges to execute the command
        database_user = settings.DATABASES['default']['USER']
        database_password = settings.DATABASES['default']['PASSWORD']
        # ============================================================
        
        # define the directory where the backup should be stored
        backup_directory = settings.BASE_DIR / 'backup'
        backup_filename = f'{database_name}_full_backup_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.sql'
        
        # Create backup command
        command = f'mysqldump --user={database_user} --password={database_password} --databases {database_name} --skip-lock-tables --skip-add-drop-table > {os.path.join(backup_directory, backup_filename)}'
        # command = f'mysqldump --user="{database_user}" --password="{database_password}" --databases "{database_name}" > {os.path.join(backup_directory, backup_filename)}'
        
        # Execute backup command
        subprocess.run(command, shell=True)
        print(f'Full MySQL backup for {database_name} created in: {backup_directory}, name: {backup_filename}')
