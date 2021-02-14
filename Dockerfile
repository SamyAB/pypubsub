FROM python:3.9-alpine

COPY . /app
RUN pip install /app
RUN rm -rf /app

CMD ["python", "-m", "pypubsub"]
