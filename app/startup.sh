#!/bin/bash
/etc/init.d/mysql start && 
echo "create database cmdb" | mysql -uroot -p123456a &&
python manage.py makemigrations &&
python manage.py migrate &&
echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'root@example.com', '123456a')" | ./manage.py shell &&
python manage.py runserver 172.17.0.2:80
wait
