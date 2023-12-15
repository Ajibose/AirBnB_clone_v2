#!/usr/bin/python3
"""
    Define a funcion that generates a .tgz archive from the contents 
"""
from datetime import datetime
from fabric.api import run

def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    currenttime = datetime.now().strftime("%Y%m%d%H%M%S")
    res = run(f"tar -cf web_static_{currenttime}.tgz web_static/")
    if res.exited == 0:
        return None
    else:
        return f"web_static_{currenttime}.tgz"
    
