#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""


from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """return the archive path if the archive has been correctly generated."""
    if os.path.isdir('versions') is True:
        return None
    else:
        local("sudo mkdir versions")
        now = datetime.now()
        timeformat = now.strftime("%Y%m%d%H%M%S")
        new_file = "versions/web_static_{}.tgz".format(timeformat)
        local("sudo tar -czvf {} web_static".format(new_file))
        return new_file