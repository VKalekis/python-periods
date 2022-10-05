FROM python:3.10

ADD app.py .

RUN pip install python-dateutil

ENTRYPOINT ["python", "./app.py"]