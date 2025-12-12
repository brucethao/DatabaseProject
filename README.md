# DatabaseProject
1. Make sure PyCharm and MySQL Workbench are installed. You will need to log into MySQL Workbench. 
2. Clone the repository into Pycharm.
3. Set up configuration.
      - The project requires a virtual environment. It is recommended to set up a new one. This can be accomplished in the terminal, *which differs depending on the system*, or within PyCharm Settings. If using PyCharm to set up the virtual environment, go into <ins>Settings</ins>, under <ins>Python</ins> -> <ins>Interpreters</ins> ->  <ins>Add Interpreter</ins> -> <ins>Add Local Interpreter</ins> -> <ins>Click Ok</ins>.
      - Afterwards, install Django into the virtual environment. In the terminal, run the command:

              pip install django
          
      - Then, install PyMySQL:
          
              pip install pymysql
          
      - Lastly, install mysqlclient:

              pip install mysqlclient
        
 4. In <ins>ZooManagementSystem/settings.py</ins> change the database password to your MySQL ```root``` user's password.
 5. You need to create a local database. In MySQL Workbench, open a new query tab or use the provided *Group_8_Database_Script* and run the single line:
    
    ```create database if not exists zoomanagement;```
    
 7. Migration files have already been created. Simply apply them. In PyCharm, run the command:

        python manage.py migrate
    
 9. Then, create an admin user with the command:

        python manage.py createsuperuser
    
 11. Now open the *Group_8_Database_Script* in MySQL Workbench if you haven't already and run the entire script.
 12. Next open the provided *Group_8_Prepopulate* in MySQL Workbench and run the entire script for initialization of data.
 13. You should now be able to run the webpage. In PyCharm, run the command:

         python manage.py runserver
     
 15. Click on the server link in the terminal. *Congrats you have a running webpage for Lakeside Zoo!*
