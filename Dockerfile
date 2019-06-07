FROM python:3.7-alpine

LABEL version="1.0" description="SB Admin 2 Dash" maintainer="chris@cjadkins.com"

RUN mkdir -p /app
COPY requirements.txt /app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . .

EXPOSE 8050
CMD ["gunicorn","-w","2","--bind",":8050","SB_Admin_2:app.server"]