# DatabaseProject
# 1. Make sure PyCharm and MySQL Workbench are installed properly. You will need to log into MySQL Workbench. 
# 2. Clone the repository into Pycharm.
# 3. Set up configuration:
#      - The project requires a virtual environment. It is recommended to set up a new one. This can be done with the terminal or the PyCharm IDE UI. If using the UI, Go into Settings, under Python -> Interpreters -> Add Interpreter -> Add Local Interpreter -> Click Ok.
#      - Now we need to install Django into the v.e. 
#          - Either use the terminal command: pip install django 
#          - Or in Zootopia/views.py, hover over one of the 'from django' lines at the top which it should be underlined, and it will give you an option to install Django.
#      - You will also need to install PyMySQL: 
#          - Either use the terminal command: pip install pymysql
#          - Or hover over the import pymysql and click download pymysql located in the ZooManagementSystem/__init__.py file.
#      - To use MySQL with Django use the command: pip install mysqlclient
# 4. In ZooManagementSystem/settings.py change the database password to your MySQL root user password.
# 4. Open the provided database script in MySQL Workbench and run the two lines:
#      - create database if not exists zoomanagement;
#      - use zoomanagement;
# 5. In PyCharm use the command: python manage.py migrate
# 6. Create a superuser with the command: python manage.py createsuperuser
# 7. Go back to the database script and run the entire script.
# 8. Open the provided prepopulate sql file and run the entire script.
# 9. You should now be able to run the webpage. Use the command: python manage.py runserver
# 10. Click on the server in the terminal. Congrats you have a running webpage for Lakeside Zoo!
