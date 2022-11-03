FROM python:3.9

WORKDIR /app

COPY ./* /app
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV GRADIO_SERVER_PORT=8989
