# Real-Estate-Site
Users can search for property according to their requirements and can send inquiry to the realtor owner. Users can also track their inquiries in their dashboard.

## Installing
* Start a virtual environment
```virtualenv env <environment name>```\
```source <environment name>/bin/activate```
* Install all the dependencies
```pip3 install -r requirements.txt``` (Linux)\
```pip install -r requirements.txt``` (Windows)
* Create a superuser
```python3 manage.py createsuperuser``` (Linux)\
```python manage.py createsuperuser```(Windows)
* Make migrations and migrate
For Windows:
```python manage.py makemigrations```\
```python manage.py migrate```
For Linux:
```python3 manage.py makemigrations```\
```python3 manage.py migrate```

## Running the project
```python3 manage.py runserver``` (Linux)\
```python manage.py runserver``` (Windows)

## Built with 
* Python 3.8
* Django 2.1.1
