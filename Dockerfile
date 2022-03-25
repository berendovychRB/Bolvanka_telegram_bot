FROM python:3.8

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR app

COPY . .

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

RUN chmod +x src/main.py

CMD python3 src/main.py;