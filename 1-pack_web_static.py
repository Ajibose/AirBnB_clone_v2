#!/usr/bin/python3
"""
    Define a funcion that generates a .tgz archive from the contents
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    currenttime = datetime.now().strftime("%Y%m%d%H%M%S")

    # os.makedirs("versions", exist_ok=True)
    local("mkdir -p versions")
    res = local(f"tar -cf versions/web_static_{currenttime}.tgz web_static")
    if res.succeeded:
        return res
    else:
        return None
