#!/usr/bin/env python

import os
import subprocess
import datetime

USERNAME = '#####GITHUB_USERNAME######'
GITHUB_URL = 'https://github.com/{}'.format(USERNAME)
#This should be changed to the directory where your Github_Autoupload folder is
DIR_PATH = os.path.dirname('/Users/abanks/Projects/Github_AutoUpload/')

os.chdir(DIR_PATH)
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
        git_add = subprocess.call(['git', 'add', '.'])
        if git_add != 0:
            err_comm1 = ('Something went wrong, return value of {}'.format(git_add))
            subprocess.call('echo', err_comm1)
            continue
 
        git_commit = subprocess.call(['git','commit','-m',str(datetime.datetime.now())])
        if git_commit == 0:
            print('+'*50)
            print('commiting changes for '+r)
            print('+'*50)

        elif git_commit == 1:
            print('='*50)
            print(r+' is up-to-date')
            print('='*50)
            continue
        else:
            print('Something went wrong with the commit, return value of {}'.format(git_add))
            continue
 
        git_push = subprocess.call(['git', 'push', 'origin', 'master'])
        if git_push == 0:
            print('+'*50)
            print(r+' changes pushed to master')
            print('+'*50)
        else:
            print('/`\`'*50)
            print("Error: couldn't push commit for "+r+' return value of\
                  {}'.format(git_push))
            print('/`\`'*50)

