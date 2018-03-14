# Intro to Backend Development in Python
**Presented by: George Ke and Abhijeet Prasad**

Hi there! Please do the following pre-reqs below before the workshop so we can get started right away! Feel free to message us if you have any issues. Also like our [Facebook Page](https://www.facebook.com/uwblueprint/) and check out our [website](https://www.uwblueprint.org/)!

**Slides:** [Slides](https://docs.google.com/presentation/d/1v-2YcJB7gdWSbYjeqB6z0F6B3GSZxJmkCJeksxXgt3U/edit)

**Additional Resources:** 
- https://www.python.org/
- http://flask.pocoo.org/
- https://www.sqlite.org/index.html
- https://en.wikipedia.org/wiki/Front_and_back_ends

## Set up

1. Downloading the code
	- For Git
		1. Install Git at https://git-scm.com/download
		2. Open command line and run 
			- `git clone https://github.com/uwblueprint/intro_to_backend_development_in_python.git`
			- `cd intro_to_backend_development_in_python`
	- Download a zip 
		1. Click green button that says "Clone or download" on the right above this read me
		2. Download the zip of this repository and unzip
		3. Open command line and cd into this directory.
		
2. Setting up Python (Rest of the setup is in command line and in the project directory)
	1. Make sure Python 2.7.0 or higher is installed by running `python --version`
		- If you don't have python go here: https://www.python.org/downloads/
	2. Install pip
		- In the root directory of this project you should see a file called `get-pip.py`
		- Run `python get-pip.py`
		- Verify install was successful with `pip --version`

3. Set up a virtual environment (env). 
	- For MacOS or Linux users:
		- `sudo pip install virtualenv`
	- For Ubuntu users:
		- `sudo apt-get install python-virtualenv`
	- For Windows users:
		- Install easy_install
		- Run same commands as above without "sudo"

4. Creating the virtual environment (Make sure you're in the root directory of this project)
	- `cd starter`
	- `virtualenv env`

5. Activate your venv (Make sure you're in the `starter` directory)

	- For MacOS or Linux users:
		- `. env/bin/activate`
	- For Ubuntu users:
		- `source venv/bin/activate`
	- For Windows users:
		- `env\Scripts\activate`
		
6. Download required files. Run `pip install -r requirements.txt`

7. Export `FLASK_APP` env variable
	- For MacOS, Linux or Ubuntu users:
		- `export FLASK_APP=app.py`
	- For Windows Users:
		- `set FLASK_APP=app.py`
		
8. Run Flask:`flask run`
	- Alternative method: `python -m flask run`

9. Go to your web browser and go to the url `127.0.0.1:5000`. You should see something interesting!
