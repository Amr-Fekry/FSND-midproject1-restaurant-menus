# [FSND](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) mid-project1 - Restaurant Menus

This is a basic data-driven web application that allows a user to perform CRUD operations (Create/Read/Update/Delete) on a list of restaurants and their menus.

Server functionality is applied twice using two different approaches:
1. lower level python's built-in [http.server](https://docs.python.org/3.7/library/http.server.html) library.
2. higher level python's [flask](http://flask.pocoo.org/) framework.

Both servers are connected to the same SQLite database which is setup and manipulated through SQLAlchemy ORM.

### Requirements:
1. [Python3](https://www.python.org/downloads/) (version 3.7.1 was used)
2. Install external dependencies: `pip3 install -r requirements.txt`

### Usage:
- to run the python server:
  - `cd python_server/`
  - `python python_server.py`
- to run the flask server:
  - `cd flask_server/`
  - `python flask_server.py`
