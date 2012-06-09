#!/usr/bin/python
from fabric.api import local, abort
from fabric.contrib.console import confirm

def commit():
    local('git add -p && git commit')

def push():
    if not confirm('Do you really want to push your changes?'):
        abort('Aborting at user request')
    local('git push -u origin master')

def cp():
    commit()
    push()
