# Real-Estate-Site
Users can search for property according to their requirements and can send inquiry to the realtor owner. Users can also track their inquiries in their dashboard.

## Installing
 * Start a virtual environment
```
virtualenv env <environment name>
source <environment name>/bin/activate
```
* Install all the dependencies
```
pip3 install -r requirements.txt
``` 
* Create a superuser
```
python3 manage.py createsuperuser
```
* Make migrations and migrate
```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Running the project
```
python3 manage.py runserver
```

### In windows use ```python``` instead of ```python3``` and ```pip``` instead of ```pip3``` in all the commands.

## Built with 
* Python 3.8
* Django 2.1.1
