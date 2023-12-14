#!/usr/bin/env bash
# Prepare the web server
if ! command -v nginx &> /dev/null; then
	apt-get -y update
	apt-get -y install nginx
	utf allow 'Nginx HTTP'
	service nginx start
fi

mkdir -p "/data/"
mkdir -p "/data/web_static/"
mkdir -p "/data/web_static/releases/"
mkdir -p "/data/web_static/shared/"
mkdir -p "/data/web_static/releases/test/"

str="<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"
echo -e "$str" > "/data/web_static/releases/test/index.html"

ln -fs "/data/web_static/releases/test/" "/data/web_static/current"
chown -R "ubuntu:ubuntu" "/data/"

sed -i '/server_name _;/r /dev/stdin' /etc/nginx/sites-available/default <<EOF
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
EOF

service nginx restart
