
# credits to: https://nander.cc/using-selenium-within-a-docker-container

FROM python:3.8

# default and allow for overides to script arguments
ARG APP_URL=http://172.17.0.1
ENV APP_URL=$APP_URL

ARG SCRIPT_NUM_LOOPS=1
ENV SCRIPT_NUM_LOOPS=$SCRIPT_NUM_LOOPS

COPY . /app
COPY gen/MANIFEST /app
WORKDIR /app

RUN mkdir __logger

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["sh", "-c", "cat MANIFEST && ./wait-until-ready.sh ${APP_URL} && python -u ./app.py -u $APP_URL -n $SCRIPT_NUM_LOOPS"]
