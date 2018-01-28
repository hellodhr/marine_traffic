FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY vessel_spider ./

WORKDIR /usr/src/app/vessel_spider
COPY *.csv ./

CMD ["scrapy crawl vessel", "-o vessel.json"]