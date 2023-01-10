Ensembl Django DBCopy portable App
==================================

Ensembl DBCopy service support Database manager

Quick start
-----------

1. Create a project

Check out repo from github


2. Create an app within your project

    2.1 Init your app
    
    ```run ./manage.py migrate ensembl_dbcopy```

    2.2 Register your new app: Edit  your_project_name/settings/base.py
     
    ```python
    #... 
    INSTALLED_APPS = [
        #...
        'ensembl.production.dbcopy',
        #...
    ]
    ```

    2.3 Check: 
       
    ```shell script 
    ./manage.py check 
   ```
 
Quick start with docker 
-------------------------
1. Build Docker Image
    ```
    sudo docker build -t dbcopy  . 

    ```
2.  Mirage the changes to DB
    ```
    sudo docker run --env DBNAME=dbcopy --env DBUSER=ensembl --env DBPASS=test --env DBHOST=localhost --env DBPORT=3306  -it --network=host dbcopy:latest /usr/src/app/src/manage.py migrate
    
    if mysqlsever in remote host use param --add-host

    sudo docker run  --add-host <remote hostname>:<ip address>  --env DBNAME=dbcopy --env DBUSER=ensembl --env DBPASS=test --env DBHOST=<remote hostname> --env DBPORT=3306 -p 8000:8000  dbcopy:latest /usr/src/app/src/manage.py migrate

    ```

3. Run dev server
    ```
    sudo docker run --env DBNAME=dbcopy --env DBUSER=ensembl --env DBPASS=test --env DBHOST=localhost --env DBPORT=3306 -p 8000:8000  dbcopy:latest /usr/src/app/src/manage.py runserver 0.0.0.0:8000

    if mysqlsever in remote host use param --add-host

    sudo docker run --add-host <remote hostname>:<ip address> --env DBNAME=dbcopy --env DBUSER=ensembl --env DBPASS=test --env DBHOST=<remote hostname> --env DBPORT=3306 -p 8000:8000  dbcopy:latest /usr/src/app/src/manage.py runserver 0.0.0.0:8000
    
    ```

4. Run dbcopy container with guincorn
    ```
    sudo docker run --env DBNAME=dbcopy --env DBUSER=ensembl --env DBPASS=test --env DBHOST=localhost --env DBPORT=3306 -p 8000:8000  dbcopy:latest

    ```    

