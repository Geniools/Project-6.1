# Sports accounting

## Introduction

*Sports accounting* is an open source application developed by IT2B group at NHL Stenden University of Applied
Sciences in Emmen, The Netherlands. The application is developed part of Project 6.1 for *Quintor*.

The application consists of a *base application* which contains the basic functionality and requirements of the
application. In addition, several *add-ons* are developed which extend the functionality of the
base application. The entire application is build with python using the web framework Django.

Moreover, the application contains an API which can be used to retrieve data from the application.

**For more information over the application, please refer to our Design Document.**

## Installation

### Prerequisites

- python 3.9 or higher (venv - optional)
- Django 4.0 or higher
- django-rest-framework
- pip
- git
- mysql: 8.0.26 or higher
- mongodb

### Installation

1. Clone the repository

`` git clone <repository_link>``

2. Install the requirements

`` python -m pip install -r requirements.txt ``

3. Create a database in *mysql* and *mongodb*
4. Navigate to ``Project6.1/src/sports_accounting/`` and create a file called `local_settings.py`
   and add the following lines:

```
# Copy this file to local_settings.py and fill in the required information.
# The following file contains the local settings for the application.
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Whenever the site should be on debug or not
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret! (for development can be anything)
SECRET_KEY = '<security_key>'

# When DEBUG is False, in case of a code error, the ADMINS will be notified on their email address.
ADMINS = []

# Static files
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

# Credentials for the NoSQL DB
MONGO_DB_PASSWORD = "<database_password_mongoDB>"
# You can use the password above in the URI connection below
MONGO_DB_URI = "<uri_connection_to_mongoDB>"

```

5. In your favourite terminal, navigate to the project folder containing the manage.py file (``Project6.1/src/``)
   and run the following commands:

`` python manage.py makemigrations ``

`` python manage.py migrate ``

6. Create a superuser (after running the command above fill in the required information when prompted)

`` python manage.py createsuperuser ``

7. Run the server and replace <PORT> with the port you want to run the server on (default is 8000 if not specified)

`` python manage.py runserver <PORT> ``

8. Navigate to ``http://localhost:<PORT>`` in your browser to view the application.

## Usage

In order to login to the admin panel of the application navigate to
``http://localhost:<PORT>/admin`` and login with the credentials of the superuser you created in step 6.

- The admin panel can be used to add, edit and delete data from the application.
- You can create other users and assign them to a group/permission.

To upload an MT940 file, navigate to ``http://localhost:<PORT>/mt940/upload`` and upload one or multiple files.

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

#### Available formats

The API supports the following formats:

- json
- xml
- api (browsable API)

To change the format, add the following to the url:

``?format=<format>``

#### Additional information

The API will offer the same permissions as the admin panel. This means that a user with the ``member``
role will have read-only permissions and a user with the ``treasurer`` role will have read and write
permissions (to specific parts of the application).

By default, the API can be viewed in the browser as a browsable API. This means that you can navigate
through the API and see the available endpoints and their functionality.

- For more information about the permissions, please refer to the *User Roles* section.

### User Roles

The application contains 3 roles:

1. **Member** -> can only view data from the application (has read-only permissions)
2. **Treasurer** -> can view, edit specific data from the application and upload MT940 files
3. **Admin** (*superuser*) -> treasurer role + can manage other users and their roles and other permissions
   regarding deleting and adding data in the database
4. **Staff** -> can log in the admin panel (used in combination with the other roles)

**The roles mentioned above together apply both to the admin panel and to the
available API.**