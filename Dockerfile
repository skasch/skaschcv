FROM tiangolo/uwsgi-nginx-flask:python3.7

EXPOSE 80

ENV SKASCHCV_PORT 80

COPY app /app
RUN cd /app & pip install -r requirements.txt
