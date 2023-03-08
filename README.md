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

Go to adoptProject/settings.py and add `rest_framework`, `accounts`, `pets`, and `adoption` to INSTALLED_APPS

Next, create the models...

Accounts,
Adoptions,
Pets



side note: to use django-rest-framework browsable API:
`pip install markdown`
`pip install django-filter`

...add `rest_framework` to INSTALLED_APPS AdoptProject settings.py

next, go to urls.py of AdoptProject and add:
`from django.urls import path, include`
`path('api-auth/', include('rest_framework.urls'))`

next, add configuration dictionary REST_FRAMEWORK into adoptProject settings.py

```
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```


To run django:
`python manage.py runserver`