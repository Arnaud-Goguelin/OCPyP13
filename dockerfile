FROM python:3.12.3

WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]