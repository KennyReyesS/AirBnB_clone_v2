#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy:
"""


from fabric.api import put, env, sudo
import os


env.user = 'ubuntu'
env.hosts = ['34.139.28.87', '54.164.112.178']


def do_deploy(archive_path):
    if os.path.isfile(archive_path) is False:
        print("no se encontro")
        return False
    else:
        archive_split = archive_path.split('/')
        with_extension = archive_split[1]
        rm_extension = with_extension.split('.')
        name_archive = rm_extension[0]
        print("poniendo archivo")
        put(archive_path, "/tmp/{}".format(with_extension))
        print("creando carpeta con archivo")
        sudo("mkdir -p /data/web_static/releases/{}/".format(name_archive))
        print("descomprimiendo")
        sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            with_extension, name_archive))
        print("eliminando archivo de tmp")
        sudo("rm /tmp/{}".format(with_extension))
        print("moviendo archivo")
        sudo("mv /data/web_static/releases/{}/web_static/* "
             "/data/web_static/releases/{}/".format(
                 name_archive, name_archive))
        print("eliminando archivo que movi")
        sudo("rm -rf /data/web_static/releases/{}/web_static".format(
            name_archive))
        print("eliminando carpeta current")
        sudo("rm -rf /data/web_static/current")
        print("enlace simbolico")
        sudo("ln -s /data/web_static/releases/{}/ "
             "/data/web_static/current".format(name_archive))
        return True
