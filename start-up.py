# This Python file uses the following encoding: utf-8
import os, sys
import pandas as pd
import csv
from datetime import datetime, timedelta, date

def createRep():
    if(os.path.exists("./data") == False):
        os.system('mkdir ./data')
        #file = open("./data/")
    os.system('wget https://lyaonq.am.files.1drv.com/y4mxH96WBKsE8JsACXScFsJ-dw4AFSi70uPnpleVaBYNnjbH_wFl1DRIwe1hjNcnvJZ8j459FYUFuGWYIOWI8VK0Ma_AzDrACvkJLNSM1NkwPaz3BMPlN-ArLZqiA5vOeEktZXwFEvw9HMPiVr2Kq3B1lG-04-votzdwOnq_BtZKYP7jcAZcH2oeLLSI6FVyL1b07WkQybBeMkdMm-uFdOjag')
    #Move to 
    os.system('mv y4mxH96WBKsE8JsACXScFsJ-dw4AFSi70uPnpleVaBYNnjbH_wFl1DRIwe1hjNcnvJZ8j459FYUFuGWYIOWI8VK0Ma_AzDrACvkJLNSM1NkwPaz3BMPlN-ArLZqiA5vOeEktZXwFEvw9HMPiVr2Kq3B1lG-04-votzdwOnq_BtZKYP7jcAZcH2oeLLSI6FVyL1b07WkQybBeMkdMm-uFdOjag ./data/sante.txt')
    manageDf()

def manageDf():
    os.system('du -h ./data/sante.txt')
    os.system('cat --5 ./data/sante.txt')
    data = pd.read_csv('./data/sante.txt', sep="\t", names=["age", "sexe", "typedouleur", "sucre", "tauxmax", "angine", "depression"])
    print(data)

###------------------------------------------------------------- START HERE 

createRep()
