# MNIST training Docker image

## Building
```
cd <container path>
docker build . -t mnist-dev -f ./Dockerfile
```

## Running
Usage:
```
docker run -it mnist-dev bash
```

### Output
This docker image is used to train and produce mnist_model output which then is deployed into streamlit app. It was used only once for building the model.