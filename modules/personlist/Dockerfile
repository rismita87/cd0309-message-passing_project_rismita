FROM python:3.9-alpine
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 50089
CMD ["python", "./udaconnect/personlist_provider.py"]