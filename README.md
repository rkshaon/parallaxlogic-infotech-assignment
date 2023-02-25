# Assignment

## Required
- Python 3.10.6

## Steps
First create a virtual environment

```python3 -m venv env```

Activate virtual environment

```source env/bin/activate``` (Linux)

Clone the project

```git clone https://github.com/rkshaon/parallaxlogic-infotech-assignment.git```

Install dependencies

```pip install -r requirements.txt```

Create database in PostgreSQL named `test`

To migrate

```python3 manage.py makemirgations```

```python3 manage.py migrate```

Run project

```python3 manage.py runserver```
