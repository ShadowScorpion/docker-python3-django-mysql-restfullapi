# Realization of Django with MySQL and RESTFullAPI on Python3

Original **python** image on [DockerHub](https://hub.docker.com/_/python/).

### How to build and run image

- Clone this repo
```
git clone https://github.com/ShadowScorpion/docker-python3-django-mysql-restfullapi.git
```

- Change location to cloned folder
```
cd ./docker-python3-django-mysql-restfullapi
```

- Build image
```
docker build --no-cache -t image-name .
```

- Run image

    1. Run test Django application with RESTFullAPI
        ```
        docker run -d image-name
        ```
    2. Run test Django application with RESTFullAPI with forwarding of ports
        ```
        docker run -d -p 80:80 image-name
        ``` 
    3. Run your own application of Django
        ```
        docker run -d -p 80:80 image-name -v /path_to_application:/app
        ```
        * When application has been mounted, Docker will migrate all changes of Django to MySQL

### Usage

- Get MySQL
    ```
    mysql -uroot -p
    ```
        * Docker will set "123456a" as password of root user to MySQL


- Get admin page
    ```
    http://host/admin
    ```
        * Docker will set "123456a" as password of root user to Django

- Get API page of Django
    ```
    http://host/components/api/server
    http://host/components/api/os
    ```
