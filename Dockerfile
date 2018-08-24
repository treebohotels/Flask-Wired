FROM python:3.7.0-slim

COPY flask_wired flask_wired
COPY setup.py setup.py
RUN python -m venv venv
RUN venv/bin/pip install -e .

COPY sample_app sample_app
WORKDIR sample_app
RUN ../venv/bin/pip install -r requirements.txt
RUN ../venv/bin/pip install gunicorn

RUN chmod +x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
