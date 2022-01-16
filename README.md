# Stock Company CRUD API
This is a test repository for Flink recruitment process made by Alejandro Pérez.

# Run the project in local
1. Create a venv and activate it
2. Install the requirements  
~~~
pip install -r requirements.txt  
~~~
3. Start the Django server  
~~~
python3 manage.py runserver
~~~  
4. If needed, make migrations
~~~
python3 manage.py makemigrations
~~~  
~~~
python3 manage.py migrate
~~~  
5. Use the home page url `localhost:8000/`  

You will see the the home page with the paths we can use and how to use them


# Validate code linter  
In order to implement PEP8 in this project, it was used Flake8 library to check the code. You can check it too with the next command in the terminal:  
~~~
flake8
~~~
  
# Run tests  
To run tests and coverage report just use the django test command  
~~~
python3 manage.py test
~~~  
  
