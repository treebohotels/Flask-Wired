FROM python:3.7.0-slim
#FROM python:3.7.0-alpine3.8
#RUN adduser -D flagon_user

#WORKDIR /home/flagon_user

COPY flagon flagon
COPY setup.py setup.py
RUN python -m venv venv
#RUN apk add libpq

# Installing build dependencies
#RUN apk update && \
#    apk add --virtual .build-deps gcc python-dev musl-dev postgresql-dev && \

RUN venv/bin/pip install -e .
#RUN apk del .build-deps

COPY sample_app sample_app
WORKDIR sample_app
RUN ../venv/bin/pip install -r requirements.txt
RUN ../venv/bin/pip install gunicorn

#USER flagon_user
RUN chmod +x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
