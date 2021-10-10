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


#### 4.5 Adding login template to the demo page

        modified:   README.md
        modified:   apps/main/templates/demo.html


#### 4.6 Loading static files

        modified:   README.md
        modified:   apps/main/templates/demo.html
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   tamplate/demo.html

        NOTE: Moved static fiels from root to main app


#### 4.7 Create admin login page with new logo - Views, Templates and Urls

        modified:   README.md
        new file:   apps/main/static/assets/img/INGStore.png
        new file:   apps/main/templates/admin/signin.html


#### 4.8 Create admin base template

        modified:   README.md
        new file:   apps/main/templates/admin/base.html
        new file:   apps/main/templates/admin/navbar.html
        new file:   apps/main/templates/admin/sidebar.html


#### 4.9 Create admin dashboard home page for admin

        modified:   README.md
        new file:   apps/main/admin_views.py
        new file:   apps/main/static/assets/img/favicon.png
        new file:   apps/main/static/assets/img/favicon1.png
        new file:   apps/main/static/assets/img/logo.png
        deleted:    apps/main/templates/admin/navbar.html
        deleted:    apps/main/templates/admin/sidebar.html
        renamed:    apps/main/templates/admin/base.html -> apps/main/templates/template_admin/base.html
        new file:   apps/main/templates/template_admin/index.html
        new file:   apps/main/templates/template_admin/navbar.html
        new file:   apps/main/templates/template_admin/sidebar.html
        renamed:    apps/main/templates/admin/signin.html -> apps/main/templates/template_admin/signin.html
        modified:   apps/main/urls.py
        modified:   apps/main/views.py


#### 4.10 Customizing admin home page

        modified:   README.md
        new file:   apps/main/static/assets/img/favicon2.png
        new file:   apps/main/static/assets/img/logo1.png
        modified:   apps/main/templates/template_admin/base.html
        modified:   apps/main/templates/template_admin/navbar.html
        modified:   apps/main/templates/template_admin/sidebar.html
        modified:   apps/main/urls.py


#### 4.11 Admin login part 1 - HttpResponse login process

        modified:   README.md
        modified:   apps/main/templates/template_admin/signin.html
        modified:   apps/main/urls.py
        modified:   apps/main/views.py


#### 4.12 Admin login part 2 - Login and showing alert message

        modified:   README.md
        modified:   apps/main/templates/template_admin/signin.html
        modified:   apps/main/views.py


#### 4.13 Admin login part 3 - Display name/email of the LOGGED IN user

        modified:   README.md
        modified:   apps/main/templates/template_admin/navbar.html


#### 4.14 Admin logout 

        modified:   README.md
        modified:   apps/main/templates/template_admin/navbar.html
        modified:   apps/main/templates/template_admin/sidebar.html
        modified:   apps/main/templates/template_admin/signin.html
        modified:   apps/main/urls.py
        modified:   apps/main/views.py


#### 4.15 Preventing Un-authenticated user to access the admin dashboard

        modified:   README.md
        modified:   apps/main/views.py


### -------------------------------------------
### 5. ADMIN VIEWS SETUP
### -------------------------------------------


#### 5.1 Creating views_admin.py file and move the adminHome views function to it

        modified:   README.md
        deleted:    apps/main/admin_views.py
        modified:   apps/main/urls.py
        modified:   apps/main/views.py
        new file:   apps/main/views_admin.py


#### 5.2 House keeping - renaming files

        modified:   README.md
        modified:   apps/main/templates/template_admin/index.html
        modified:   apps/main/templates/template_admin/signin.html
        modified:   apps/main/views_admin.py


