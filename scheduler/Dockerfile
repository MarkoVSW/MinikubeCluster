FROM python:3.10

COPY requirements.txt requirements.txt

COPY main.py /usr/src/app/main.py

RUN pip3 install -r requirements.txt

CMD ["python", "/usr/src/app/main.py"]