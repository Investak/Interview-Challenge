#AKj Stock Portfolio Website

## Synopsis

User lands on the homepage, where he/she has two option either Login or Register. If user is registered then he/she can login via the link in navbar, after login he/she will be redirected to his/her profile where he/she will get list of his/her portfolios and on clicking on then he/she can view details of the companies in it and the performance of them in last month, last 3 month, last 6 month, last year by selection the duration and he/she can also change the company by clicking on left side where all are listed.And by clicking on Companies he/she can view all the companies along with their details and weight. Then he/she can logout.

## Installation And Setup

By default, Django applications are configured to store data into a lightweight SQLite database file. While this works well under some loads, a more traditional DBMS can improve performance in production.

In this guide, we'll demonstrate how to install and configure PostgreSQL to use with your Django.

sudo apt-get update

sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

###Create a Database and Database User And Grant all PRIVILEGES
sudo su - postgres

psql

CREATE DATABASE myproject;

CREATE USER myprojectuser WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

\q

exit

###Setup virtualenv for the project

Install the virtual environment, then create a virtual environment by command(python3)  "virtualenv name" .

Then activate with the command "source path_to_virtual_environment/bin/activate"

now install all the Python packages needed:

command : "pip install -r requirements.txt"

Now move to the directory where manage.py resides.run the following commands.

command : "python manage.py makemigerations"
command : "python manage.py migerate"
command : "python manage.py createsuperuser"
command : "python manage.py runserver"



Python packages:

Babel==2.3.3
defusedxml==0.4.1
Django==1.9.5
django-allauth==0.25.2
django-crispy-forms==1.6.0
django-phonenumber-field==1.1.0
django-registration-redux==1.4
djangorestframework==3.3.3
oauthlib==1.0.3
phonenumberslite==7.3.0
Pillow==3.2.0
psycopg2==2.6.1
python3-openid==3.0.10
pytz==2016.3
requests==2.9.1
requests-oauthlib==0.6.1
simplejson==3.8.2
yahoo-finance==1.2.1

## License

A short snippet describing the license (MIT, Apache, etc.)
