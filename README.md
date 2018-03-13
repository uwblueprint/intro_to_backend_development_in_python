# intro_to_backend_development_in_python
Blueprint workshop introducing backend development in Python

Follow the steps below to set up your system:

1) Set up a virtual environment (venv)

	**Make sure Python 2.7.0 or higher is installed
	For Mac OS X or Linux users:
		$ sudo pip install virtualenv
	For Ubuntu users:
		$ sudo apt-get install python-virtualenv
	For windows users:
		1) Install easy_install
		2) Run same commands as above without "sudo"

2) Make a project and create a venv

	$ mkdir [directory name]
	$ cd [directory name]
	$ virtualenv venv

3) Activate your venv

	For Mac OS X or Linux users:
		$ . venv/bin/activate
	For Ubuntu users:
		$ source venv/bin/activate
	For Windows users:
		$ venv\Scripts\activate

	** To deactivate:
		$ deactivate

4) Download required files

	$ pip install requirements.txt

5) Export FLASK_APP env variable

	For Mac OS X or Linux or Ubuntu Users:
		$ export FLASK_APP=app.py
	For Windows Users:
		$ set FLASK_APP=app.py

6) Run flask

	$ flask run

    Alternative method:
	$ python -m flask run

7) Curl

	$ curl 127.0.0.1:5000
