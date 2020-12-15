FROM python:3.7.2-slim

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

EXPOSE 8501

WORKDIR /app
COPY container/requirements.txt .
COPY utils .
COPY app.py .
COPY .aws .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV AWS_CONFIG_FILE=/app/.aws/config 
ENV AWS_SHARED_CREDENTIALS_FILE=/app/.aws/credentials

ENTRYPOINT [ "streamlit", "run"]
CMD ["app.py"]