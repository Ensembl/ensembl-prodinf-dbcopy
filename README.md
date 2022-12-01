Ensembl Django DBCopy portable App
==================================

Ensembl DBCopy service support Database manager

Quick start
-----------

1. Standalone application / testing / contributing

- Clone our repo from github
- Initialise database

   ```mysql
   CREATE USER 'ensembl'@'localhost' IDENTIFIED BY '';
   CREATE DATABASE `db_copy`;
   ```

- Run you server

   ```shell
   run ./manage.py migrate
   run ./manage.py runserver
   ```


2. As a portable app
 
- Add following requirements

```shell
pip install git+https://github.com/Ensembl/ensembl-prodinf-dbcopy.git@1.7.0#egg=ensembl-prodinf-dbcopy
```

- Register your new app: Edit  your_project_name/settings/base.py
     
```python
#... 
INSTALLED_APPS = [
  #...
  'ensembl.production.dbcopy',
  #...
]
```

- Create database tables

```shell
./manage.py migrate
```

- Define mandatory settings in your app `settings.py` 

```python
# User/password for introspect queries
INTROSPECT_DB_USER="ensro"
INTROSPECT_DB_PASS=""
```

- Check: 

```shell 
./manage.py check 
```   
 
