FROM python:3.10
WORKDIR /app
COPY ./app ./app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python app/lr.py
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8006"]
