#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy:
"""


from fabric.api import put, env, run
import os


env.user = 'ubuntu'
env.hosts = ['34.139.28.87', '54.164.112.178']


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
