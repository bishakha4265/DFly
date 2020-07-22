FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install python3-pip -y

COPY requirements.txt requirements.txt
RUN mkdir ~/Code
ADD . ~/Code
RUN pip3 install -r requirements.txt
WORKDIR ~/Code
CMD ["python3","app.py"]
