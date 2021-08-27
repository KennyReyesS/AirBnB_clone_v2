#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy:
"""


import os
from fabric.api import local, put, env, run
from datetime import datetime


env.user = 'ubuntu'
env.hosts = ['34.139.28.87', '54.164.112.178']


def do_pack():
    """return the archive path if the archive has been correctly generated."""
    if os.path.isdir("versions") is False:
        local("mkdir versions")
    now = datetime.now()
    timeformat = now.strftime("%Y%m%d%H%M%S")
    new_file = "versions/web_static_{}.tgz".format(timeformat)
    executed = local("tar -cvzf {} web_static".format(new_file))
    if executed.failed:
        return None
    else:
        return new_file


def do_deploy(archive_path):
    """ Script that distributes an archive to my web servers"""
    if os.path.isfile(archive_path) is False:
        return False

    archive_split = archive_path.split('/')
    with_extension = archive_split[1]
    rm_extension = with_extension.split('.')
    name_archive = rm_extension[0]
    if put(archive_path, "/tmp/{}".format(with_extension)).failed:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(
            name_archive)).failed:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            with_extension, name_archive)).failed:
        return False
    if run("rm /tmp/{}".format(with_extension)).failed:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(
                name_archive, name_archive)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".format(
            name_archive)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(name_archive)).failed:
        return False
    return True


def deploy():
    """creates and distributes an archive to my web servers"""
    pack_file = do_pack()
    if pack_file is None:
        return False
    else:
        call_deploy = do_deploy(pack_file)
        return call_deploy
