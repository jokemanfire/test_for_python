#! /usr/bin/env python

from fabric.api import *

env.usr = 'ubuntu'
env.password = 'hudingyang123'
env.host = '123.206.129.82'

@runs_once 
def local_task():
    local("uname -a")

def remote_task():
    with cd("/home/ubuntu"):
        run("ls -l")