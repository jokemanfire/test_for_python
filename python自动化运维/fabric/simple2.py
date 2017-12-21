from fabric.api import *

env.user = 'ubuntu'
env.password = 'hudingyang123'
env.hosts = ['123.206.129.82']

@runs_once
def input_raw():
    return prompt("please input directory name:",default="/home")

def worktask(dirname):
    run("ls -l"+dirname)

@task
def go():
    getdirname = input_raw()
    worktask(getdirname)