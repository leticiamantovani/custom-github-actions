FROM python:alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY notifier ./notifier

ENTRYPOINT ["python", "-m", "notifier.main"]
