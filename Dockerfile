FROM python:3.12-slim

RUN apt-get update && apt-get install -y python3 python3-pip curl 

RUN pip3 install uv uvicorn
WORKDIR /app
COPY pyproject.toml uv.lock /app/
RUN pip install --upgrade pip
RUN pip install .

COPY .env .
COPY src /app/src/

CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
