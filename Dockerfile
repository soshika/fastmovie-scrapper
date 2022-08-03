FROM ubuntu:latest

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV APP_HOME /usr/src/app

WORKDIR /$APP_HOME

COPY . $APP_HOME/

# RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
#     echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories
# RUN apk update
# RUN apk add make automake gcc g++ subversion python3-dev
# RUN apk add --update --no-cache g++ gcc libxslt-dev
# RUN apk add chromium chromium-chromedriver
# RUN apk add --no-cache --virtual .build-deps gcc libc-dev libxslt-dev && \
#     apk add --no-cache libxslt && \
#     pip install --no-cache-dir lxml>=3.5.0 && \
#     apk del .build-deps
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    rm -rf /var/lib/apt/lists/*
RUN add-apt-repository universe
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get -y update
RUN apt-get install -y ffmpeg
# RUN pip3 install --upgrade pip
# RUN pip3 install beautifulsoup4
# RUN pip3 install wheel
# RUN pip3 install selenium
RUN pip3 install -r requirements.txt
# RUN pip3 install --ignore-installed beautifulsoup4
# CMD tail -f /dev/null
CMD python3 cnama-seriedownloader.py