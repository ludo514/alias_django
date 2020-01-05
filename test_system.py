import os
import subprocess
from sys import argv

os.system("mkdir {}".format(argv[1]))
os.chdir("{}".format(argv[1]))
os.system("virtualenv env")
os.system("django-admin startproject base")
os.system('cmd /k "env\\Scripts\\activate.bat && pip install Django && cd base && python manage.py startapp {}"'.format(argv[1]))
