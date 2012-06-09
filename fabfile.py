#!/usr/bin/python
from fabric.api import local

def commit():
    local('git add -p && git commit')

def push():
    local('git push -u origin master')

def cp():
    commit()
    push()
