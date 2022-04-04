FROM python:3.8

RUN mkdir /usr/src/app
COPY requirements.txt /usr/src/app/

RUN cd /usr/src/app \
 && pip install --upgrade pip \
 && pip install -r requirements.txt


WORKDIR /usr/src/app

# cache model
COPY model.py model.py 
RUN python3 model.py

COPY main.py main.py

EXPOSE 8080

ENTRYPOINT uvicorn main:app --port 8080 --host 0.0.0.0
