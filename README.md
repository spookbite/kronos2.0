# kronos2.0

This webapp displays previous year's grade distribution. It has been hosted with streamlit as an app but is still under development.

You can go [here](https://kronos.streamlit.app/) for the live version of the project. Make your choices wisely :)

You can find the container image [here](https://hub.docker.com/repository/docker/spookbite/kronosv2).

# Setup 

## (Without Docker)

### Install virtual environment module
```shell
pip install virtualenv
```

### Create a virtual environment (say env) 
```shell
python -m venv env
```

### Activate the virtual environment 
```shell
env\Scripts\activate
```

### Install Dependencies 
```shell
pip install -r requirements.txt
```

Run the following code on your terminal:
```shell
streamlit run app.py
```

## Using Docker

### Pull the Docker image
```shell
docker pull spookbite/kronosv2:latest
```

### Run the container
```shell
docker run -p 8501:8501 spookbite/kronosv2
```

### You can change the {PORT}:8501 to your desired PORT.

## Credits

This project is inspired by [metakgp/kronos](https://github.com/metakgp/kronos).
