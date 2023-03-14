# Mamma_app

## Basic information:

by default api has 2 endpoints:


  - GET `/`
  - GET `/objects`

If you don't specify date range on `/objects` endpoint it gives you today's result as default

The nasa api has 7 days limit, so if you specify more than 7 days data range - the api handle that sequentially now (it is not effective, and it is space for improvement).

## Tools:

This api uses [fastapi](https://fastapi.tiangolo.com/) framework. It also uses Poetry for dependency management and Pydantic for data model definition

## prerequisites:

You will need python 3.10 on your device

- use [official documentation](https://www.python.org/downloads/) to install it

Ths project uses poetry as tool for dependency management.

- you need to install poetry. [Here](https://python-poetry.org/docs/#installation) is how to do it from official documentation.

You need to register on [nasa api](https://api.nasa.gov/) to get api token

- if you have done registration - you need to rename "env.example file" (or create .env file on your own)
and paste it there you api token

You also need docker if you want to run app locally with Docker

- you can install it [here](https://docs.docker.com/get-docker/)

## How to build it and run it locally

- First create virtual environment using poetry

use poetry shell in root directory - this creates virtual environment for you:

```shell
poetry shell
```

- To install it dependencies use poetry install in this virtual environment

```shell
poetry install
```

- To run it locally use this command in root directory:

```shell
python -m uvicorn mamma_app.app:app --reload
```

## How to build it and run it using Docker

- you can build docker image running this command:

```shell
docker build -t mamma_app:latest .
```

- Then you can run it using this command:

```shell
docker run -p 8000:8000 mamma_app
```

The API should wait for you on port 8000
