FROM ubuntu:14.04  
MAINTAINER jubin "jubin@gmail.com"
RUN apt-get update
RUN apt-get install -y python3
COPY example.py /usr/local/hello/
WORKDIR /usr/local/hello/
RUN python3 example.py -fn Jubin -ln Yadlapalli
