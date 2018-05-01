FROM python:3.5.5
MAINTAINER Antonio Silva "a.silva@pointerbp.nl"

ENV PROJECT_PATH /code

RUN mkdir -p $PROJECT_PATH
ADD requirements.txt $PROJECT_PATH/
WORKDIR $PROJECT_PATH
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . $PROJECT_PATH

CMD ["python", "app.py"]