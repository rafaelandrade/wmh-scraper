FROM --platform=linux/amd64  python:3.9

WORKDIR /code
EXPOSE 8080

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable && apt-get install -y --no-install-recommends curl

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN apt-get install curl -y

ADD . .

RUN chmod 777 health.sh

HEALTHCHECK --interval=5m --timeout=3s \
  CMD bash health.sh || exit 1

COPY . .

CMD [ "python3", "./run.py" ]
