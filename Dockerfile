FROM python:3.9-slim

WORKDIR /app

RUN mkdir -p /app/assets
RUN mkdir -p /app/classes

COPY requirements.txt run.py ./
COPY assets/ ./assets/
COPY classes/ ./classes/

RUN python3 -m pip install --upgrade pip && python3 -m pip install --no-cache-dir --user -r requirements.txt

CMD ["sh", "-c", "python3 -u /app/run.py"]
