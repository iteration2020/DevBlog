FROM openjdk:20
FROM python:3.11

ENV PYTHONDONTWRYTEBYTECODE 1
ENV PYTHOUNBEFFERED 1

RUN pip install --upgrade pip
COPY blog/requrements.txt .

RUN pip install -r requrements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
