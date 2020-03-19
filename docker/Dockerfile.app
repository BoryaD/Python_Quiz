FROM python:3.8-buster
WORKDIR /opt/project
COPY requirements.txt .
RUN pip install -r requirements.txt
