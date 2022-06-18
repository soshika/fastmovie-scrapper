FROM python:3.9-alpine

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV APP_HOME /usr/src/app

WORKDIR /$APP_HOME

COPY . $APP_HOME/

RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories
RUN apk update
RUN apk add chromium chromium-chromedriver
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade pip3
RUN pip3 install BeautifulSoup4
RUN pip3 install selenium
RUN pip3 install -r requirements.txt

CMD tail -f /dev/null
CMD python3 digimovie-moviedownloadScrapper.py