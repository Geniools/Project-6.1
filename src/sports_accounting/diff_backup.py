import subprocess
import datetime

# Set MySQL credentials and database name
mysql_user = 'root'
mysql_password = 'password'
mysql_dbname = 'sports_accounting'

# Set backup directory and filename
backup_dir = 'C:/my/backup/dir'
now = datetime.datetime.now()
backup_filename = f'{mysql_dbname}_diff_backup_{now.strftime("%Y-%m-%d_%H-%M-%S")}.sql'

# Create backup command
backup_command = f'mysqldump --user={mysql_user} --password={mysql_password} --databases {mysql_dbname} --skip-lock-tables --skip-add-drop-table > {backup_dir}/{backup_filename}'

# Execute backup command
subprocess.run(backup_command, shell=True)
print(f'Differential backup for {mysql_dbname} created successfully: {backup_dir}/{backup_filename}')
