FROM python:3.9-alpine
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 50051
CMD ["python", "./app/colour_provider.py"]