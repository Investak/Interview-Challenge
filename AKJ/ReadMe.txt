Instructions for application: "VisualOne"
(Assuming Windows system)

1. Install python 2.7 and pip in windows system.
	Guide: https://www.youtube.com/watch?v=QhevHKBy7Hc

2. Install reqiured plugins
	a.open command prompt
	b.go to desktop: cd Desktop
	c.install virtual env in desktop : pip install virtualenv 
	(make sure you have pip installed)
	d.create virtual env: virtualenv "venv_name"
	e.go to "venv_name" (run: cd "venv_name")
	f.run: .\Scripts\activate, in here we have to install pluging.(run: "pip freeze" to see the installed plugins)
	g.copy requirements.txt in this folder (not via cmd prompt)
	h.Install the following
		django
		crispy-forms
		registration-redux
		psycopg2
		yahoo-finance
	i.run this command to install via requirements.txt : pip install -r requirements.txt

3.Create project in this folder : .\Scripts\django-admin.py startproject "project_name"
	(if u have different versions of python, then this might cause some error)
	rename "project_name" to "src" (optional)

4.Using my source code ("AKJChallenge") to run the application
		
5.Setting up database
	a.We are going to use postgresql, so install it in your system and remember the username and password while installation.
	http://www.enterprisedb.com/products/pgdownload.do#windows
	b.After installing open pgadmin3 and create a database in it and remember this name. 
	c.Next, go to "src" and inside "project_name" find settings.py , go to DATABASES, and change databse name, username and password
	d.Now we are ready to run the server

6.To run the server, In the cmd prompt:
	a.Go to Desktop, then go to the folder where venv is created
	b.run: .\Scripts\activate
	c.now go to src : cd src
	d.run: python manage.py runserver
	
7.Create superuser: python manage.py createsuperuser
	Admin page:
	http://127.0.0.1:8000/admin/
	
8.Migrate models
	a.run: python manage.py makemigrations
	b.then, run: python manage.py migrate
	
		(With this command all of our tables are created without any data, now we need to add data.Since i couldn't make use of 
		yahoo-finance API,i populated the database from files.)
			(To get more data, go to http://finance.yahoo.com/q/hp?s=GE&a=03&b=1&c=2016&d=03&e=21&f=2016&g=d
			select the stock and date for the data and download the csv file at the bottom of table.
			Now edit this csv file by removing the first row, and inserting a column in first position for serial number(id).)

9.Go to pgadmin3->database->schema->public->tables 
	table_name(right-click)->import->select file from "Required Spreadsheets"(yahoo for visualiser_yahoo)->select type as csv->import.
	Also import company to visualiser_company for company list.

		I have included the csv files used for this application.
		Need to import 19 files like this.(Sorry for the inconvenience.)
		
10.We have data in database and the only thing to do is to manipulate data to generate chart.

11.When modifying or adding static files:
	run: python manage.py collectstatic

12.Now our website is ready.
	Home
	About
	Contacts

13.Login using superuser or any other user to view company list and homescreen and our application "VisualOne"

14.While registering email will not be sent but we can activate account by copying activation key of that account as superuser
	and go to this link to activate account. 
	http://127.0.0.1:8000/accounts/activate/"activation-key"

15.After selecting VisualOne,select stocks from left side to generate their graphs.
		Reset button to reset the graph.
		
	**To get intersecting lines, try Baidu and Illumina or Intel and Vodafone.
	



