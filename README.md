# mysqlbackup

Python script to make MySQL backups.

## Description

This script is not recommended for use at work level since the database connection data is in plain text within the script.

This code is a basic example of how to make backups from Python without external packages.

## Usage

In order to run the script:

```python
python3 mysqlbackup.py
```

## Local variables

Inside the script you will see the following local variables:
| Name          | Value |
|:--------------|:------|
| DB_HOST       | (`str`) IP or name of mysql server.                                                        |
| DB_PORT       | (`str`) MySQL server listening port.                                                       |
| DB_USER       | (`str`) MySQL user with the necessary permissions to make backups of the database.         |
| DB_PASS       | (`str`) mysql user password                                                                |
| DATABASES     | (`tuple`) List of the databases that you want to make backup copies of.                    |
| BACKUP_FOLDER | (`str`) Folder where you want to store the databases.                                      |
| LOG_FOLDER    | (`str`) Folder where you want to store the logs.                                           |
| LOG_FILE      | (`str`) Name of the file with which the logs will be created, **do not add an extension**. |
| LOG_LEVEL     | (`str`) Recording level of the logs, **it must be INFO**.                                  |
| LOG_RETENTION | (`int`) Days that the log files will be stored on your server.                             |
| DATE          | (`str`) Format of the date that will be added to the name of the log file and the backup.  |
