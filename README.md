# films
Start app.
## 1.Сlone repo
```
git clone git@github.com:nat1905/films.git
```

## 2.create venv for Python 3.9 and activate it
```
python -m venv venv
source venv/Scripts/activate
```
## 3.install dependecies
```
pip install -r requirements.txt
```

## 4. go to /films_library and make migrations
```
python manage.py makemigrations
python manage.py migrate
```

## 5. create superuser
```
python manage.py createsuperuser
```
## 6. run server
```
python manage.py runserver
```
