# kronos2.0

This webapp displays previous year's grade distribution. It has been hosted with streamlit as an app but is still under development.

You can go [here](https://share.streamlit.io/spookbite/kronos2.0/main/app.py) for the live version of the project. If this doesn't work, you can go [here](https://kronosv2.herokuapp.com/) as well. Apologies if both doesn't work, issue will be rectified soon :)

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

## With Docker

### Pull the Docker image
```shell
docker pull spookbite/kronosv2:2.0
```

### Run the container
```shell
docker run -p 8501:8501 spookbite/kronosv2
```

### You can change the {PORT}:8501 to your desired PORT.

## Credits

This project is inspired by [metakgp/kronos](https://github.com/metakgp/kronos).
