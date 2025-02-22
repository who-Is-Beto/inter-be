FROM python:3.10
EXPOSE 80
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD [ "gunicorn", "-b", "localhost:80", "app:create_app()" ]