FROM openjdk:20
FROM python:latest

ENV PYTHONDONTWRYTEBYTECODE 1
ENV PYTHOUNBEFFERED 1

RUN pip install --upgrade pip
COPY ./requrements.txt .

RUN pip install -r requrements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
