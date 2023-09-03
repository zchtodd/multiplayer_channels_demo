FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/

RUN mkdir -p /usr/src/app/

CMD ["daphne", "multiplayer_channels_demo.asgi:application", "-u", "/usr/src/app/daphne.sock"]
