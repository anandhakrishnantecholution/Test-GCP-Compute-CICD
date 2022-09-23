FROM python:3.8

RUN apt-get update
COPY requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app
WORKDIR /app
EXPOSE 5003
ENTRYPOINT [ "python3" ]
CMD [ "server.py" ]