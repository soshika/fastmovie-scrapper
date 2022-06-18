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
RUN pip3 --version
RUN pip --version
RUN python --version
RUN python3 --version
RUN pip install --upgrade pip
RUN pip install BeautifulSoup4
RUN pip install selenium
RUN pip install -r requirements.txt
RUN pip install --ignore-installed beautifulsoup4
CMD tail -f /dev/null
CMD python digimovie-moviedownloadScrapper.py