# Use venv

`python3 -m venv venv-open-lms`

# Change prompt

`PS1="\W $ "`

# Activate venv

`source venv-open-lms/bin/activate`

# Install Flask

`python3 -m pip install flask`


Result: 

```
Collecting flask
  Downloading https://files.pythonhosted.org/packages/f2/28/2a03252dfb9ebf377f40fba6a7841b47083260bf8bd8e737b0c6952df83f/Flask-1.1.2-py2.py3-none-any.whl (94kB)
    100% |████████████████████████████████| 102kB 1.4MB/s 
Collecting Werkzeug>=0.15 (from flask)
  Downloading https://files.pythonhosted.org/packages/cc/94/5f7079a0e00bd6863ef8f1da638721e9da21e5bacee597595b318f71d62e/Werkzeug-1.0.1-py2.py3-none-any.whl (298kB)
    100% |████████████████████████████████| 307kB 861kB/s 
Collecting itsdangerous>=0.24 (from flask)
  Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting click>=5.1 (from flask)
  Downloading https://files.pythonhosted.org/packages/d2/3d/fa76db83bf75c4f8d338c2fd15c8d33fdd7ad23a9b5e57eb6c5de26b430e/click-7.1.2-py2.py3-none-any.whl (82kB)
    100% |████████████████████████████████| 92kB 2.8MB/s 
Collecting Jinja2>=2.10.1 (from flask)
  Downloading https://files.pythonhosted.org/packages/7e/c2/1eece8c95ddbc9b1aeb64f5783a9e07a286de42191b7204d67b7496ddf35/Jinja2-2.11.3-py2.py3-none-any.whl (125kB)
    100% |████████████████████████████████| 133kB 2.3MB/s 
Collecting MarkupSafe>=0.23 (from Jinja2>=2.10.1->flask)
  Downloading https://files.pythonhosted.org/packages/98/7b/ff284bd8c80654e471b769062a9b43cc5d03e7a615048d96f4619df8d420/MarkupSafe-1.1.1-cp37-cp37m-manylinux1_x86_64.whl
Installing collected packages: Werkzeug, itsdangerous, click, MarkupSafe, Jinja2, flask
Successfully installed Jinja2-2.11.3 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 flask-1.1.2 itsdangerous-1.1.0
```

# Check if Flask has been installed

`python3`

then:

`import flask`

# Make new dir

`mkdir open-lms`

cd `open-lms`

# Make a new file

`touch open-lms.py`

# Minimalist application

[Quickstart — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart)

# Set the Flask app environment

`export FLASK_APP=open-lms.py`

# Run flask

`flask run`

Open the server on http://127.0.0.1:5000

You run Flask now in production mode. Each time you make a change, the server has to be stopped and started again via `flask run`.

You can change stuff on the fly, by using flask debug mode.

To enable flask debug, use:

`export FLASK_DEBUG=1`

If you add to the file `open-lms.py` you can also run the file directly via python.

```
if __name__ == '__main__':
    app.run(debug=True)     
```

So now you can run:

`python3 open-lms.py`

# The most popular forms is WTF

So install:

`python3 -m pip install flask-wtf`

Then create a `requirements.txt` file:

```
(venv-open-lms) open-lms $ python3 -m pip freeze > requirements.txt
(venv-open-lms) open-lms $ cat requirements.txt 
click==7.1.2
Flask==1.1.2
Flask-WTF==0.14.3
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==1.1.1
pkg-resources==0.0.0
Werkzeug==1.0.1
WTForms==2.3.3
```

# Use for CSR-protection:


Create a random number:

```
(venv-open-lms) open-lms $ python3
Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import secrets
>>> secrets.token_hex(16)
'7e002078a3859c9c0628a4f3700e935a'
```

# Gebruik je WTF formlulieren en doen je aan email-validatie:

In je code:

`from wtforms.validators import Email`

Installeer email_validator`

`python3 -m pip install email_validator`


