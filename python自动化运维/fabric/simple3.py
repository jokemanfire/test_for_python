from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = 'root'
env.geteway = '192.168.56.131 '
env.hosts = ['123.206.129.82']
env.passwords = {
    'ubuntu@123.206.129.82':'hudingyang123'
    'root@192.168.56.131':'a123456'
}

lpackpath = '/home/hu/test.txt'
rpackpath = '/home/ubuntu/install'

@task
def put_task():
    run("mkidr -p /home/ubuntu/install")
    with settings(warn_only=True):
        result = put(lpackpath,rpackpath)
    if result.failed and not confirm("put file failed, Continue[Y/N]?"):
        abort("Aborting file put task!")
