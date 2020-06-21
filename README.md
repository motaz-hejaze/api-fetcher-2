# api-fetcher-2

requirements:
-----------------
  - python >= 3.6
  - virtualenv
  - Git
------------------

* first clone the repo:
  - git clone https://github.com/motaz-hejaze/api-fetcher-2.git


* cd into cloned folder:
  - cd api-fetcher-2

* create virtual environmet:
  - virtualenv venv -p python3.6
  
* activate your virtual environment:
  - source venv/bin/activate (linux)

* install required python packages:
  - pip install -r requirements.txt

* create database and tables:
  - cd project/
  - python manage.py makemigrations api_fetcher
  - python manage.py migrate

* create superuser:
  - python manage.py creasuperuser

* runserver:
  - python manage.py runserver

* within your browser , go to http://127.0.0.1:8000/
