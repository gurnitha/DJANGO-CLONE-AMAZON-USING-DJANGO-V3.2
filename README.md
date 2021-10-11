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


#### 5.3 Create category_list page (Views, Templates, and Urls)

        modified:   README.md
        new file:   apps/main/templates/template_admin/category_list.html
        modified:   apps/main/urls.py
        modified:   apps/main/views_admin.py


#### 5.4 Create category_create form page Part 1 - Views, Template and Urls basic

        modified:   README.md
        new file:   apps/main/templates/template_admin/category_create.html
        modified:   apps/main/urls.py
        modified:   apps/main/views_admin.py


#### 5.5 Create category_create form page Part 2 - customizing the page

        modified:   README.md
        modified:   apps/main/templates/template_admin/category_create.html


#### 5.6 Create category_create form page Part 3 - adding scripts to pre-populated the slug field

        modified:   README.md
        modified:   apps/main/templates/template_admin/base.html


#### 5.7 Create get_absolute_url on Categories model to create cagegory

        modified:   README.md
        modified:   apps/main/models.py
        modified:   apps/main/urls.py
        new file:   media/5fa58abe1df1d5001821952e.jpg
        new file:   media/5fa58abe1df1d5001821952e_J7ihZmY.jpg


#### 5.8 Create alert message for success and error on creating category

        modified:   README.md
        modified:   apps/main/templates/template_admin/base.html
        modified:   apps/main/views_admin.py
        new file:   media/50fdbd11700123e6ff11b830dfcb3740.jpg


#### 5.9 Adding alert error messsage if any form field of creating category is empty

        modified:   README.md
        modified:   apps/main/templates/template_admin/category_create.html


#### 5.10 Styling the error message

        modified:   README.md
        modified:   apps/main/templates/template_admin/base.html
        modified:   apps/main/templates/template_admin/category_create.html


#### 5.11 Customizing the Category Create form width

        modified:   README.md
        modified:   apps/main/templates/template_admin/category_create.html


#### 5.12 Displaying categories to category_list page

        modified:   apps/main/templates/template_admin/category_list.html


#### 5.13 Adding Active switcher button to category card

        modified:   README.md
        modified:   apps/main/templates/template_admin/category_list.html


#### 5.14 Adding conditional to Active switcher button

        modified:   README.md
        modified:   apps/main/templates/template_admin/category_list.html


#### 5.15 Creatge Update category page Part 1 - Views, Tempate and Urls

        modified:   README.md
        modified:   apps/main/templates/template_admin/category_list.html
        new file:   apps/main/templates/template_admin/category_update.html
        modified:   apps/main/urls.py
        modified:   apps/main/views_admin.py


#### 5.16 Creatge Update category page Part 2 - adding form template

        modified:   README.md
        modified:   apps/main/templates/template_admin/category_update.html


#### 5.17 Creatge Update category page Part 3 - showing field values to the form

        modified:   README.md
        modified:   apps/main/templates/template_admin/category_update.html


#### 5.18 Creatge Update category page Part  - showing the current thumbnail in the form field

        modified:   README.md
        modified:   apps/main/templates/template_admin/category_update.html


#### 5.19 Limiting description's text

        modified:   README.md
        modified:   apps/main/templates/template_admin/category_list.html
        new file:   media/toys.jpg


#### 5.20 Sidebar Part 1 - Modified sidebar menu and add link

        modified:   README.md
        modified:   apps/main/templates/template_admin/sidebar.html


#### 5.21 Sidebar Part 2 - Add active state to the menu

        modified:   README.md
        modified:   apps/main/templates/template_admin/sidebar.html


#### 5.22 Sidebar Part 3 - Add active state to the menu for Update category

        modified:   README.md
        modified:   apps/main/templates/template_admin/base.html
        modified:   apps/main/templates/template_admin/sidebar.html


### -------------------------------------------
### 6. SUB CATEGORIES
### -------------------------------------------


#### 6.1 Create Urls, Views and basic templates for SubCategoriesList, SubCategoriesCreate and SubCategoriesUpdate

        modified:   README.md
        modified:   apps/main/templates/template_admin/sidebar.html
        new file:   apps/main/templates/template_admin/subcategory_create.html
        new file:   apps/main/templates/template_admin/subcategory_list.html
        new file:   apps/main/templates/template_admin/subcategory_update.html
        modified:   apps/main/urls.py
        modified:   apps/main/views_admin.py


#### 6.2 SubCategoriesCreate Part 1- Adding template

        modified:   README.md
        modified:   apps/main/templates/template_admin/subcategory_create.html


#### 6.3 SubCategoriesCreate Part 2- Adding options with conditional to select a category and create a subcategory

        modified:   README.md
        modified:   apps/main/models.py
        modified:   apps/main/templates/template_admin/subcategory_create.html
        new file:   media/5fa58abe1df1d5001821952e_N1aH0xW.jpg


#### 6.4 SubCategoriesList - Add template to show list of subcategories

        modified:   README.md
        modified:   apps/main/templates/template_admin/subcategory_list.html
        new file:   media/toys_fnkJNBX.jpg


#### 6.5 Display message after creating a new subcategory

        modified:   README.md
        modified:   apps/main/views_admin.py
        new file:   media/vIqzOHXj.jpg


#### 6.6 Display subcategory parent in the subcategorieslist

        modified:   README.md
        modified:   apps/main/templates/template_admin/subcategory_list.html


#### 6.7 SubCategoriesUpdate Part 1- Adding template

        modified:   README.md
        modified:   apps/main/templates/template_admin/subcategory_update.html