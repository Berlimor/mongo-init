FROM python:3.10-slim

COPY . .

RUN pip install pymongo

ENTRYPOINT ["python3", "mongo.py"]
