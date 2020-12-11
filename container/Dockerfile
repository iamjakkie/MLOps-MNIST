FROM python:3.7.2-slim

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

EXPOSE 8501

WORKDIR /app
COPY container/requirements.txt .

RUN pip install --upgrade pip
RUN pip install streamlit
RUN pip install -r requirements.txt
RUN pip install opencv-python

COPY app.py .
COPY classify.py .
COPY ./MNIST/mnist_model ./MNIST/mnist_model
ENTRYPOINT [ "streamlit", "run"]
CMD ["app.py"]