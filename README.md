# marine_traffic
A collection of spiders to crawl data from http://www.marinetraffic.com

## Usage
Make sure to create an isolated Python 3.x environment (using [virtualenv](https://virtualenv.pypa.io/en/stable/userguide/#usage) or [conda](https://conda.io/docs/user-guide/tasks/manage-environments.html#)) before running the code
```
# get source code
mkdir marine_traffic
cd marine_traffic
git clone https://github.com/slangenbach/marine_traffic.git

# create isolated environment using virtualenv
pip install virtualenv
virtualenv <name of your environment>
source activate <name of your environment>/bin/activate
pip install -r requirements.txt

# alternatively use conda
conda env create -n <name of your environment>
source activate <name of your environment>
conda env update -f marine_traffic.yml
```
The crawler automatically reads an input file (CSV) from the top vessel_spider directory
By default, the second column of the file is used to extract vessel identification IDs (IMO) for crawling
```
# copy input file to target directoy
cd vessel_spider
cp -v <path to your your input file> .

# start crawler
scrapy crawl vessel -o <output>.json
```

## Problem
Given a list of vessel identification IDs (IMO), e.g. 9632143, retrieve general information under vessel particulars for specific vessels from https://www.marinetraffic.com, store information in data structure and write full result to JSON file or database

## Solution
* Read IMOs from input file, e.g. CSV
* Query information for each IMO via [search url](https://www.marinetraffic.com/en/ais/index/search/all?keyword=)
* Access [result page](https://www.marinetraffic.com/en/ais/details/ships/shipid:3409595/mmsi:219630000/vessel:9632143)
* Parse general information
* Store information in data structure
* Write data structure to JSON file or database

## Open points
* Generate start urls from input file :white_check_mark:
* Improve handling of search result page :white_check_mark:
* Clean parsed data :white_check_mark:
* Add Python environment configuration :white_check_mark:
* Add tests based on ~~[pytest](https://docs.pytest.org/en/latest/)~~ [Scrapy contracts](https://doc.scrapy.org/en/latest/topics/contracts.html) :under_construction:
* Enable continous integration via [Travis CI](https://travis-ci.org) :construction:
* Isolate app in Docker container :construction:
* Include instructions for running containerized app on heroku, AWS, Azure and GCP
* Add spider to parse port data :construction: