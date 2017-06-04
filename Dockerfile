FROM python:3
MAINTAINER skrypnyk.kostiantyn <skrypnyk.kostiantyn@gmail.com>

### Login as a root ###
USER root


### Updating the system ###
RUN apt-get update -y && apt-get upgrade -y


### Setting Default password on MySQL ### 
RUN echo "mysql-server mysql-server/root_password password 123456a" | debconf-set-selections

RUN echo "mysql-server mysql-server/root_password_again password 123456a" | debconf-set-selections


### Installing needed requiremets ###
ENV requirements="build-essential python-dev python-setuptools \ 
		python3-pip mysql-server mysql-client libmysqld-dev"  

RUN apt-get install $requirements -y && rm -rf /var/lib/apt/lists/*


### Installing pip packages ###
ENV prequirements="django djangorestframework django-filter mysqlclient patterns"

RUN pip install $prequirements


###  Get Django application ###
ENV APP_DIR /app

RUN mkdir ${APP_DIR} 

COPY app ${APP_DIR}

WORKDIR ${APP_DIR}

### Starting MySQL and creation of database ###

RUN chmod +x ./startup.sh

CMD ["./startup.sh"]
