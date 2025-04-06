# Polling System Project

This mini-project allowed me to use Django for the first time to create a polling system.

## Prerequisites

Before running this project locally, ensure you have the following installed:

* IDE (VS Code, PyCharm, etc.)
* Install Python 3.10+ version > for type hinting compatability
* Install Django ([click here for instructions](https://www.djangoproject.com/))

## Lessons Learned

This project was completed in several phases:

### Part 1: Project Setup

1. Go to root directory
2. Create subfolder: `mkdir <directory_name>`
3. Create project: `django-admin startproject <project_name> <directory_name>`
4. Development server: `python3 manage.py runserver`
5. Create app: `python3 manage.py startapp polls`

A basic view was then created by updating the `polls/view.py`, `polls/urls.py`, and `mysite/urls.py` files.

It's important to know that Django exposes a secret key inside `mysite/settings.py` by default. If this wasn't simply a project saved locally, then it would be important to hide this value, preferabbly as an environmental variable. 

### Part 2: Models & Database Setup

1. Database setup: `python3 manage.py migrate`
2. Creating models: update `polls/models.py`
3. Activating models: edit INSTALLED_APPS in `mysite/settings.py`, run `python3 manage.py makemigrations polls`
4. Apply models to database: `python3 manage.py migrate`
5. Console API model interaction: `python3 manage.py shell`
6. Create admin user: `python3 manage.py createsuperuser`
7. Register model on admin interface: update `polls/admin.py`
8. User admin database interface: `python3 manage.py runserver`

### Part 3:

1. Views: update `polls/views.py`
2. Templates: create in `polls/templates/polls` directory

## Credits

The following resources helped me complete this project:

* [Django (Getting Started)](https://docs.djangoproject.com/en/5.2/intro/): Tutorial walkthroughs for app.