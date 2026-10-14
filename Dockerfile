FROM python:3.11-slim

WORKDIR /app

COPY task2.py .

RUN pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python", "task2.py"]
