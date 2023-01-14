FROM python:3.8.7
COPY . /my-micro/main
WORKDIR /my-micro/main
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT  main:main