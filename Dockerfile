FROM python:3.9

ENV VIRTUAL_ENV=/usr/local
WORKDIR /app
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN apt-get update && apt-get install -y postgresql-client
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY etl.py etl.py

CMD ["python", "etl.py"]