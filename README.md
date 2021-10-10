### CLONE AMAZON USING DJANGO V3.2


### -------------------------------------------
### 1. INITIAL SETUP
### -------------------------------------------


#### 1.1 Create virtualenv and local repository

        new file:   .gitignore
        new file:   README.md


### -------------------------------------------
### 2. CREATE DJANGO PROJECT AND APP
### -------------------------------------------


#### 2.1 Create django project called 'config'

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2.2 Create django app 'main' 

        modified:   README.md
        new file:   apps/main/__init__.py
        new file:   apps/main/admin.py
        new file:   apps/main/apps.py
        new file:   apps/main/migrations/__init__.py
        new file:   apps/main/models.py
        new file:   apps/main/tests.py
        new file:   apps/main/views.py


#### 2.3 Register the 'main' app to the project

        modified:   README.md
        modified:   apps/main/apps.py
        modified:   config/settings.py


### -------------------------------------------
### 3. DATABASE USING MYSQL
### -------------------------------------------


#### 3.1 Install mysqlclient

        modified:   README.md


#### 3.2 Create database and setup django-environ

        modified:   .gitignore
        modified:   README.md
        modified:   config/settings.py


#### 3.3 Create models and run migrations

        modified:   README.md
        new file:   apps/main/migrations/0001_initial.py
        modified:   apps/main/models.py
        modified:   config/settings.py


#### 3.4 Register models to admin

        modified:   README.md
        modified:   apps/main/admin.py
        modified:   apps/main/models.py


### -------------------------------------------
### 4. ADMIN TEMPLATE SETUP
### -------------------------------------------


#### 4.1 Create static and media directories inside the root or src folder

        modified:   README.md


#### 4.2 Linking static and media folder with the project

        modified:   README.md
        modified:   config/settings.py


#### 4.3 Adding static assets

        ...
        new file:   static/assets/js/page/modules-vector-map.js
        new file:   static/assets/js/page/utilities-contact.js
        new file:   static/assets/js/scripts.js
        new file:   static/assets/js/stisla.js


#### 4.4 Create demo page using Views, Templates, Urls

        modified:   README.md
        new file:   apps/main/templates/demo.html
        new file:   apps/main/urls.py
        modified:   apps/main/views.py
        modified:   config/urls.py
