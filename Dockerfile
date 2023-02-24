FROM python:3.10-alpine

COPY  . /app

WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "mamma_app.app:app", "--host=0.0.0.0", "--reload"]