FROM python:2.7-onbuild

RUN python test.py

ENTRYPOINT ["python", "app.py"]
