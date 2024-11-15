FROM python:3.12.3 as base

WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

FROM base as dev

CMD ["sleep", "infinity"]

# FROM base as prod

# CMD ["gunicorn", "app.wsgi:application", "--bind"]