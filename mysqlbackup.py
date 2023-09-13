# pylint: disable=W1203
from pathlib import Path
from datetime import datetime
import logging
import subprocess
from logging.handlers import RotatingFileHandler

# Variables
## Database
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_USER = "user-change-me"
DB_PASS = "pass-change-me"
DATABASES = ("db1", "db2")
## Backup
BACKUP_FOLDER = "backups"
## LOG
LOG_FOLDER = "logs"
LOG_LEVEL = "INFO"
LOG_FILE = "mysqlbackup"
LOG_RETENTION = 31
DATE = datetime.now().strftime("%Y-%m-%d")

log_folder = Path(LOG_FOLDER)
if not log_folder.exists():
    log_folder.mkdir(parents=True, exist_ok=True)

backup_folder = Path(BACKUP_FOLDER)
if not backup_folder.exists():
    backup_folder.mkdir(parents=True, exist_ok=True)

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
log_format = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(filename)s | %(message)s"
)
info_handler = RotatingFileHandler(
    f"{log_folder}/{LOG_FILE}-{DATE}.txt",
    backupCount=LOG_RETENTION
)
info_handler.setFormatter(log_format)
logger.addHandler(info_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_format)
logger.addHandler(stream_handler)

def get_dump(ddbb):
    try:
        logger.info(f"The {ddbb} databases backup starts...")
        subprocess.run([f"mysqldump -h {DB_HOST} -P {DB_PORT} -u {DB_USER} -p{DB_PASS} {ddbb} > {backup_folder}/{ddbb}-{DATE}.sql"],
                       check=True, capture_output=True, shell=True)
    except subprocess.CalledProcessError as err:
        logger.error(f"{err.stderr}")
        subprocess.run(f"rm {backup_folder}/{ddbb}-{DATE}.sql", check=True, shell=True)
        logger.info(f"Delete the failed {ddbb} database to avoid having empty backup files.")
    else:
        logger.info(f"The backup in the {ddbb} database has finished successfully")

if __name__ == "__main__":
    for database in DATABASES:
        get_dump(database)
