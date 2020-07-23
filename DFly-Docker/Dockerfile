FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn3 -y
COPY ./DFly-Docker/requirements.txt requirements.txt
RUN mkdir ~/Code
ADD . ~/Code
RUN pip3 install -r requirements.txt
WORKDIR ~/Code

CMD ["cd ..","gunicorn3", "-b", "0.0.0.0:8000", "app:app", "--workers=5"]
