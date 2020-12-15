# MNIST streamlit app Docker Image

## Building
```
cd <mnist project path>
docker build . -t mnist-streamlit -f .\container\Dockerfile
```

## Running
Usage:
```
docker run -it -p 8501:8501 -v ${PWD}:/app mnist-streamlit
```

### Output
This docker image is used for the main application. It requires .aws folder and config+credentials files to load the updated version of the model.