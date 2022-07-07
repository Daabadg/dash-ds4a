FROM python:3.10.4
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . ./
CMD gunicorn -b 0.0.0.0:80 app.app:server

#docker build -t dash_app .
#docker image ls
#docker run -p 8080:80 dash_app