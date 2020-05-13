import os
from sys import argv

try:
    os.system("mkdir {}".format(argv[1]))
    os.chdir("{}".format(argv[1]))
    os.system("touch {}.js".format(argv[2]))
    os.system("npm init && npm i body-parser && npm i express && npm i dotenv")
    os.system("echo const express = require('express') > {}.js".format(argv[2]))
    os.system("echo const http = require('http') >> {}.js".format(argv[2]))
    os.system("echo const bodyParser = require('body-parser') >> {}.js".format(argv[2]))
    os.system("echo const app = express() >> {}.js".format(argv[2]))
    os.system("echo app.use(bodyParser.urlencoded({ extended: true })) >> " + argv[2] + ".js")
    os.system("echo app.listen(3000, function()) >> {}.js".format(argv[2]))
except IndexError:
    print("Erreur entrer")