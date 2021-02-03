FROM python:3.7.4

RUN apt-get update && apt-get install -y \
        gcc \
        libsasl2-dev \
        libldap2-dev \
        libssl-dev \
        gettext \
        vim \
        zip \
        xmlsec1 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /tmp
WORKDIR /tmp
RUN pip install --upgrade pip
RUN pip install -r requirements.txt \
	&& mkdir /tmp/excel_file \
	&& mkdir /tmp/excel_file/data_schema \
	&& mkdir /tmp/excel_file/export_files

WORKDIR /
