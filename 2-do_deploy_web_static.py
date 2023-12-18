#!/usr/bin/python3
"""
    Distributes my web static files to the web servers
"""
import os
from fabric.api import run, env, put


env.hosts = [
        '54.237.209.252',
        '54.144.83.4'
        ]


def do_deploy(archive_path):
    """distributes an archive to  web servers"""
    if not os.path.exists(archive_path):
        return False

    env.hosts = [
            '54.237.209.252',
            '54.144.83.4'
            ]

    env.user = "ubuntu"

    filename = os.path.basename(archive_path)
    print(filename)
    file_no_ext = os.path.splitext(filename)[0]
    print(file_no_ext)
    r = put(archive_path, "/tmp/")
    run(f"sudo mkdir -p /data/web_static/releases/{file_no_ext}/")
    run(f"sudo tar -xzf /tmp/{filename} -C "
        f"/data/web_static/releases/{file_no_ext}/")
    # run(f"mv /data/web_static/releases/{file_no_ext}/web_static/*
    # /data/web_static/releases/{file_no_ext}")
    run(f"sudo rm -rf /data/web_static/releases/{file_no_ext}/web_static")
    run(f"sudo rm -rf /tmp/{filename}")
    run("rm -rf /data/web_static/current")
    run(f"sudo ln -s /data/web_static/releases/{file_no_ext}/ "
        f"/data/web_static/current")
