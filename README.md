# Sports accounting

## Introduction

*Sports accounting* is an open source application developed by IT2B group at NHL Stenden University of Applied
Sciences in Emmen, The Netherlands. The application is developed part of Project 6.1 for *Quintor*.

The application consists of a *base application* which contains the basic functionality and requirements of the
application. In addition, several *add-ons* are developed which extend the functionality of the
base application. The entire application is build with python using the web framework Django.

Moreover, the application contains an API which can be used to retrieve data from the application.

**For more information over the application, please refer to our Design Document.**

## Getting started

### Prerequisites

- python 3.9 or higher
- pip
- git
- mysql (*or MariaDB*):
    - *mysqldump* (optional for database backup)
- mongodb
    - *mongodump* (optional for database backup)

### Installation

#### Quick installation - Docker

1. Make sure you have docker installed on your machine. If not, please refer to the following link:

   https://docs.docker.com/get-docker/


2. Clone the repository

   ``git clone https://github.com/Geniools/Project-6.1.git``


3. Copy the file ``example_local_settings.py`` from the root folder to ``src/sports_accounting/`` and
   rename it to ``local_settings.py``. *Do not change the contents of the file if you use the default Docker
   configuration*!


4. Navigate to the Project root folder (default `Project_6.1`). Run the following command:

   `` docker-compose build ``
   . This will build the docker images.

5. Run the following command:

   `` docker-compose up ``
   . This will start the containers (the database and the Django application).

**Note!**: *if the above command fails, or the containers do not start as expected, **run the command again**.
At first, the database takes longer to set up, so the application might not be able to connect to the database*.

6. Navigate to ``http://localhost:8000`` in your browser to view the application. Refer to the **Usage** section for
   more information.

#### Manual installation

1. Clone the repository

   `` git clone https://github.com/Geniools/Project-6.1.git``

2. Navigate to the Project root folder (default `Project-6.1`). Install the requirements using pip

   `` python -m pip install -r requirements.txt ``

3. Create a database in *mysql* and *mongodb*
    - easy way to install *MySQL* and *phpmyadmin* with docker:

      https://migueldoctor.medium.com/run-mysql-phpmyadmin-locally-in-3-steps-using-docker-74eb735fa1fc
    - easy way to install *MongoDB* with Atlas:

      https://www.mongodb.com/atlas
4. Navigate to ``Project6.1/src/sports_accounting/``, create a file named `local_settings.py`
   and add the following lines:

   ```
   # Copy this file to local_settings.py and fill in the required information.
   # The following file contains the local settings for the application.
   from pathlib import Path
   
   # The base directory of the project (default is 'src')
   BASE_DIR = Path(__file__).resolve().parent.parent
   
   # Whenever the site should be on debug or not (display errors, etc.)
   # SECURITY WARNING: don't run with debug turned on in production!
   DEBUG = True
   
   # SECURITY WARNING: keep the secret key used in production secret! (for development can be anything)
   SECRET_KEY = '<security_key>'
   
   # When DEBUG is False, in case of a code error, the ADMINS will be notified on their email address.
   ADMINS = []
   
   # Static files (css, javascript, images)
   STATIC_ROOT = "<path_to_static_folder>"
   
   # Media files
   MEDIA_ROOT = BASE_DIR / 'media'
   
   # A list of directories where Django looks for static files (must be empty if used in production)
   STATICFILES_DIRS = [BASE_DIR / 'static']
   
   # Credentials for the SQL database
   DB_PASS = "<database_password>"
   DB_USER = "<database_user>"
   DB_HOST = "<database_host>"
   DB_NAME = "<database_name>"
   DB_PORT = <database_port> # default is 3306
   
   # Credentials for the backup SQL database
   DB_BACKUP_PASS = "<database_password_backup_priviledges>"
   DB_BACKUP_USER = "<database_user_backup_priviledges>"
   
   # Credentials for the NoSQL DB
   MONGO_DB_DATABASE = "SportsAccounting"
   MONGO_DB_CLUSTER = "Transactions"
   
   MONGO_DB_PASSWORD = "<database_password_mongoDB>"
   MONGO_DB_URI = "<uri_connection_to_mongoDB>" # example: "mongodb+srv://<username>:<password>@<cluster>/<database>?retryWrites=true&w=majority"
   
   ```

5. In your favourite terminal, navigate to the project folder containing the manage.py file (``Project6.1/src/``)
   and run the following commands:

   `` python manage.py makemigrations ``

   `` python manage.py migrate ``

   **! Note: In case any of the commands above fail, try running the command again by supplying the flag
   ``--skip-checks`` at the end.**

6. Create a superuser (after running the command below fill in the required information when prompted)

   `` python manage.py createsuperuser ``

7. Run the server and replace <PORT> with the port you want to run the server on (default is 8000 if not specified)

   `` python manage.py runserver <PORT> ``

8. Navigate to ``http://localhost:<PORT>`` in your browser to view the application.

## Usage

1. In order to log in to the admin panel of the application navigate to
   ``http://localhost:<PORT>/admin`` and login with the credentials of the superuser you created in **step 6**.

    - The admin panel can be used to add, edit and delete data from the application.
    - You can create other users and assign them to a group/permission.

2. To upload an MT940 file, navigate to ``http://localhost:<PORT>/mt940/upload`` and upload one or multiple files.
3. To access the API, navigate to ``http://localhost:<PORT>/api``.

**Note: Only a ``superuser`` or a user with ``treasurer`` permissions can upload MT940 files.**

- For more information about the permissions, please refer to the *User Roles* section.

## API

The API can be used to retrieve data from the application. The API is build with Django Rest Framework.
Below is a list of all the endpoints and their functionality.

### Endpoints

#### Base application

- ``http://localhost:<PORT>/api/file/``: Retrieve all MT940 files
- ``http://localhost:<PORT>/api/file/<id>``: Retrieve a specific MT940 file
- ``http://localhost:<PORT>/api/transaction/``: Retrieve all transactions
- ``http://localhost:<PORT>/api/transaction/<id>``: Retrieve a specific transaction
- ``http://localhost:<PORT>/api/transaction-category/``: Retrieve all transaction categories
- ``http://localhost:<PORT>/api/transaction-category/<id>``: Retrieve a specific transaction category
- ``http://localhost:<PORT>/api/currency/``: Retrieve all currencies
- ``http://localhost:<PORT>/api/currency/<id>``: Retrieve a specific currency
- ``http://localhost:<PORT>/api/balance-details/``: Retrieve all balance details
- ``http://localhost:<PORT>/api/balance-details/<id>``: Retrieve a specific balance detail

#### Cash add-on

- ``http://localhost:<PORT>/api/cash-transaction/``: Retrieve all cash transactions
- ``http://localhost:<PORT>/api/cash-transaction/<id>``: Retrieve a specific cash transaction

#### Linked transaction add-on

- ``http://localhost:<PORT>/api/member/``: Retrieve all members
- ``http://localhost:<PORT>/api/member/<id>``: Retrieve a specific member
- ``http://localhost:<PORT>/api/linked-member-transaction/``: Retrieve all linked transactions
- ``http://localhost:<PORT>/api/linked-member-transaction/<id>``: Retrieve a specific linked transaction

### Available formats

The API supports the following formats:

- json
- xml
- api (browsable API)

To change the format of the displayed data, supply the url with the following parameter:

``?format=<format>``

### Additional information

The API will offer the same permissions as the admin panel. This means that a user with the ``member``
role will have read-only permissions and a user with the ``treasurer`` role will have read and write
permissions (to specific parts of the application).

By default, the API can be viewed in the browser as a browsable API. This means that you can navigate
through the API and see the available endpoints and their functionality.

- For more information about the permissions, please refer to the *User Roles* section.

## User Roles

The application contains 3 roles:

1. **Member** -> can only view data from the application (has read-only permissions)
2. **Treasurer** -> can view, edit specific data from the application and upload MT940 files
3. **Admin** (*superuser*) -> treasurer role + can manage other users and their roles and other permissions
   regarding deleting and adding data in the database
4. **Staff** -> can log in the admin panel (used in combination with the other roles)

**The roles mentioned above together apply both to the admin panel and to the
available API.**

## Backup

The application makes use of the 3rd party library *django-cron* to run scripts on a regular basis (only in production)
which perform backups of both *MongoDB* and *MySQL* database. The backups are saved to the
``Project6.1/src/backups/`` folder (folder will be created if it does not exist).

In order to perform a backup immediately you can run the following command from the terminal in the folder containing
the manage.py file:

`` python manage.py runcrons ``

# Miscellaneous

On Windows systems *python* might not be added to the **PATH** variable. In this case you will have to add it manually.
To do this, follow the steps below:

1. Open the ``Control Panel`` and navigate to ``System and Security`` -> ``System`` -> ``Advanced system settings``.
2. Click on ``Environment Variables``.
3. In the ``System variables`` section, select the ``Path`` variable and click ``Edit``.
4. Click ``New`` and add the path to the ``python.exe`` file (e.g. ``C:\Python38\``).
5. Click ``OK`` to save the changes.
6. Close all open windows and restart your terminal.
7. Run the command ``python`` in your terminal. If it works, you have successfully added python to the PATH variable.

**`mongodump` and `mysqldump` have to be added to the PATH variable as well**

If the ``python`` command is not recognized try using ``py`` instead of ``python`` on *Windows* systems.
On *Linux* systems make sure to use ``python3`` instead of ``python``.

If the ``pip`` command is not recognized try using ``python -m pip`` instead of ``pip`` on *Windows* systems
(or make sure to add `pip` to the PATH variable). On *Linux* systems make sure to use ``pip3`` instead of ``pip``.