INSTALLATION NOTES:

Locally, I have done development on a Mac OS X 10.9.5 using Bitnami Django Stack, which ships with:
  - Django 1.9.5
  - Python 2.7.11
  - Apache 2.4.20
  - PostgreSQL 9.5.2

* The public demo is running in openshift.
The openshift server was problematic to setup because of its own custom environment, so I based the project structure in these two quickstart projects:
- https://github.com/openshift/django-example (will provide the basic project setup for a django app in openshift)
- https://github.com/drivard/openshift-django-postgresql (I only took the definition of database variables in settings.py)

Additionally, the requirements couldn't be installed automatically due to server errors (as described here: http://stackoverflow.com/questions/29883879/openshift-python-pip-install-cffi-fails)
The only workaround I know so far is to log in with ssh to the openshift app and manually install:
pip install yahoo-finance==1.2.1
pip install psycopg2==2.6 

MANAGEMENT NOTES:

The fixtures included in the project provide some basic users with portfolios to view the basic functionalities.
I created the initial data from development project with:
python manage.py dumpdata --format=json PlaygroundMgmt > PlaygroundMgmt/fixtures/playground_init_data.json

To run the import command:
python manage.py import_instruments <csv_file>

I have added the one provided in the challenge as a csv in the tmp folder,
so it can be run with:
python manage.py import_instruments tmp/list.csv


BACKEND TODOs:
- Improve loading of chart data, (progressive load).
- define how the weights can be calculated and the control the user has for them.
- validation in server for valid portfolio names, avoid duplicates


FRONTEND TODOs:

- Change all alerts (these were just a quick fix to get the functionality) to react modals, possibly with this 
- Handle all Error msgs (including offline status)
- smooth animations and transitions in user interactions
- Fix for responsive design
- implement Sass or Less (according to team preference...) to organize css styles better and optimize rules-list
- add styling to search input text in instruments box

VERY BIG TODO!:
- generate unit tests and e2e tests, I haven't had enough time to create any...
- cross-browser testing, I've only tested Chrome.
- mobile design is broken due to several styles, It needs to be adjusted.

NOTES on charting lib:
before realizing that Highcharts was the preferred option (based on the LinkedIn description of skill requirements),
I started to make some tests with http://rrag.github.io/react-stockcharts/, which is a much smaller project with no 
commercial support, nevertheless I leave the link for reference in case someone might be interested, I started to get in
contact with the author, in general the lib is written with React using ES6 features.