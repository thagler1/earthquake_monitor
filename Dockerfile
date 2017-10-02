 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 run apt-get install binutils libproj-dev gdal-bin
 RUN pip install -r requirements.txt
 ADD . /code/