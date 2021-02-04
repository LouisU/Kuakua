FROM python:3.7.4

COPY ./requirements.txt /tmp
WORKDIR /tmp
RUN pip install -U pip
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com
RUN pip install -r requirements.txt

WORKDIR /
