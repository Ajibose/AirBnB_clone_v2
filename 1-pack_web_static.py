#!/usr/bin/python3
"""
    Define a funcion that generates a .tgz archive from the contents
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    currenttime = datetime.now().strftime("%Y%m%d%H%M%S")

    os.makedirs("versions", exist_ok=True)
    path = f"versions/web_static_{currenttime}.tgz"
    print(f"Packing web_static to {path}")
    res = local(f"tar -cvzf versions/web_static_{currenttime}.tgz web_static/")
    print(f"web_static packed: {path} -> {os.stat(path).st_size}")

    if res.succeeded:
        print(res)
        return res
    else:
        return None
