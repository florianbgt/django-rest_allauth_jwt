# django-rest_allauth_jwt
login, change password and user information API using django rest Json Web Token

## Dependencies:
django
djangorestframework
allauth
djangorestframework-simplejwt
corsheaders

## setup:
Create and cativate virtual environment
```
python -m venv env
env\Scripts\activate (on windows)
source env/bin/activate (linux)
```
install dependencies
```
pip install -r requirements.txt
```
make migration and migrate
```
python manage.py makemigration
python manage.py migrate
```
Create superuser
```
python manage.py createsuperuser
```
run dev server
```
python manage.py runserver
```
## API end points:
### /api/users/token
get access and refresh token

{
    "username": "",  #use email for login
    "password": ""
}

### /api/users/token/refresh
refresh access token
{
    "refresh": refresh token
}

### /api/users/password/change
Change user password (require access token)
{
    "old_password": "",
    "password": "",
    "password2": ""
}

### /api/users/profile
Change user name and email address (require access token)
{
    "id": ,
    "email": "",
    "first_name": "",
    "last_name": "",
}