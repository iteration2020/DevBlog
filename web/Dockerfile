FROM openjdk:20
FROM python:latest

ENV PYTHONDONTWRYTEBYTECODE 1
ENV PYTHOUNBEFFERED 1



RUN pip install --upgrade pip
COPY blog/requrements.txt .

RUN pip install -r requrements.txt

COPY .. .
COPY ./other_module/google_translate /usr/local/lib/python3.12/site-packages/google_translate


EXPOSE 8000

#CMD ["web", "manage.py", "runserver", "0.0.0.0:8000"]
