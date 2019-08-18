# Django Single sign-on using [mozilla-django-oidc](https://github.com/mozilla/mozilla-django-oidc)

### Installation

Export the values from `.bashrc` file and configure them according to your client.
Then run these below commands inside the main folder : 

```sh
$ pip install -r requirements.txt 
$ python manage.py makemigrations
$ python manage.py migrate
```
To start the development server :
```sh
$ python manage.py runserver
```