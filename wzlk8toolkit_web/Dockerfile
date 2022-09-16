FROM python:3.9

# install netcat
RUN apt-get update && apt install -y netcat

MAINTAINER y.zhu@wzl.rwth-aachen.de

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/var/www/html/wzlk8toolkit_web 
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

ADD . $APP_HOME

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN sed -i 's/\r//' ./start.sh

RUN chmod +x ./start.sh

ENTRYPOINT /bin/bash ./start.sh
