#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy:
"""


import os
from fabric.api import local, put, env, sudo
from datetime import datetime
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


env.user = 'ubuntu'
env.hosts = ['34.139.28.87', '54.164.112.178']


def deploy():
    """creates and distributes an archive to my web servers"""
    pack_file = do_pack()
    if pack_file is None:
        return False
    else:
        call_deploy = do_deploy(pack_file)
        return call_deploy
