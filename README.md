# AdoptMe_Django_React
AdoptMe following django-rest-framework and frontend masters React video

BACKEND SET UP 

Steps:

Set up a new environment
`python -m venv env`
`source env/bin/activate`

Once inside the virtual environment, install the package requirements 
`pip install django`
`pip install djangorestframework`


To exit virtual environment anytime: `deactivate`

Create a new project to work with
`django-admin startproject adoptProject .`

Create an app to use to create a simple web API
`python manage.py startapp accounts`
`python manage.py startapp pets`
`python manage.py startapp adoption`

Go to adoptProject/settings.py and add `rest-framework`, `accounts`, `pets`, and `adoption` to INSTALLED_APPS

Next, create the models...

Accounts,
Adoptions,
Pets


