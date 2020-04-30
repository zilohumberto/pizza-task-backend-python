FROM python:3.6.3

ENV TZ=America/Argentina/Buenos_Aires
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir /app
ADD . /app
WORKDIR /app
ENV PYTHONPATH /app/
RUN pip install -r requirements.txt