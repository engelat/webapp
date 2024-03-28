FROM python:3.9-slim-buster

LABEL Name="Python Flask Demo App" Version=1.4.2
LABEL org.opencontainers.image.source = "https://github.com/benc-uk/python-demoapp"

WORKDIR /app
COPY build/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY build/src/run.py .
COPY build/src/app .

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
