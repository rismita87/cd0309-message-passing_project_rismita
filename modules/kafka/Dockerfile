FROM python:3.9-alpine

WORKDIR .

COPY kafka_person_data_poller.py .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "kafka_person_data_poller.py"]