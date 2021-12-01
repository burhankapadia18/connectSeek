# connectSeek
A student management portal - where students can provide a username and password to gain access to college programs and other learning related materials.

Steps to make site running on your machine (using docker):
1. Make sure python3 is installed in your machine. v3.6 and above preferred
2. clone the repository on the desired location. command:git clone https://github.com/burhankapadia18/connectSeek.git
3. move into the folder which has clonned. command:cd connectSeek
4. Make sure on each step you are on path where manage.py file is present.
5. run command : docker build -t conneckseek .
6. to start container, run command : docker-compose up
7. to stop container, run command : docker-compose down

You are good to go. you can see the site on the localhost:8000 .
