#!/usr/bin/env python

import os
import subprocess
import datetime

USERNAME = '#####GITHUB_USERNAME######'
GITHUB_URL = 'https://github.com/{}'.format(USERNAME)
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

#Get repo name from hidden config file ignoring '#'
if not os.path.isfile('./.gitauto.config'):
    print('No config file is here')
    print('Creating config file @ ./.gitauto.config please edit the config')
    #create file here


F = open("./.gitauto.config", "r")

repolist = []
for line in F:
    #skip whitespace
    if line.strip():
        z = line.split()
        if z[0][0] != '#':
            repolist.append(z[0])

filelist = os.listdir(DIR_PATH)
#Check if we want these files updated
for r in repolist:
    if r in filelist:
        os.chdir(DIR_PATH+'/'+r)
        subprocess.call(['git', 'add', '.'])
        if \
        subprocess.call(['git','commit','-m',str(datetime.datetime.now())])==1:
            print('='*50)
            print(r+' is up-to-date')
            print('='*50)
            continue
        else:
            print('+'*50)
            print('pushing changes for '+r)
            print('+'*50)
        try:
            subprocess.call(['git', 'push', 'origin', 'master'])
            print('='*50) 
            print(r+' changes pushed to master')
            print('='*50)
        except:
            print('/`\`'*50)
            print("Error: couldn't push commit for "+r)
            print('/`\`'*50)

