FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip install redis
ADD /hello_front /app
