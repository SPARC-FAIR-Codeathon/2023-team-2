FROM python:3.9.2-alpine

RUN pip install --upgrade pip

RUN apk add curl

WORKDIR /api

COPY . .

RUN export FLASK_APP=app.py

RUN pip install -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

CMD ["python", "app.py"]