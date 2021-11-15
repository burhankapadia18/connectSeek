# connectSeek
A student management portal - where students can provide a username and password to gain access to college programs and other learning related materials.

Steps to make site running on your machine (on a mac machine):
1. Make sure python3 is installed in your machine. v3.6 and above preferred
2. clone the repository on the desired location. command:git clone https://github.com/burhankapadia18/connectSeek.git
3. move into the folder which has clonned. command:cd connectSeek
4. Make sure on each step you are on path where manage.py file is present.
5. Install the virtual environment. command:pip install virtualenv
6. Create a virtual environment. command:virtualenv venv
7. Activate the virtual environment. command:source venv/bin/activate
8. Install redis server. command:brew install redis (can ignore step 4)
9. Install requirements of site. command:pip install -r requirements.txt
10. Open another terminal window and start redis server. command redis-server
11. Open another terminal window, move into the connectSeek folder and start celery worker. command:celery -A connectSeek worker -l info
12. Open another terminal window, move into the connectSeek folder and start django server. command:python3 manage.py runserver

You are good to go. you can see the site on the localhost:8000 .
