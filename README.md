# librekids
Kindergarten Information and Data System

First steps

(Optional) Create Python's virtual environment: python3 -m venv <directory>
(Optional) Activate virtual environment: source <directory>/bin/activate
    The virtual environment can be deactivated later: deactivate

Rename or copy the file source/librekids/settings-sample.py to source/librekids/settings.py and edit the database section according to your system settings first.

Init database: './manage migrate'

Create superuser account (administrator): './migrate createsuperuser'

Run Django's built-in server to develop: './migrate runserver'

Access to the admin, to add some users and data: http://localhost:8000/admin

... or to the normal application: http://localhost:8000
