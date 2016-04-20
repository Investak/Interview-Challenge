A sample application

Install the virtuall environment.then make virtual environment by command(python3)  "virtualenv name" .
Then activate with the command "source path_to_virtual_environment/bin/activate"

now install all the Python packages needed:

command : "pip install -r requirements.txt"

Now move to the directory where manage.py resides.run the following commands.

"python manage.py makemigerations"
"python manage.py migerate"
"python manage.py createsuperuser"
"python manage.py runserver"



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



