# marine_traffic
A collection of spiders to crawl data from http://www.marinetraffic.com

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
* Generate start urls from input file
* Clean parsed data
* Add Python environment configuration
* Add tests based on [pytest](https://docs.pytest.org/en/latest/)
* Enable continous integration via [Travis CI](https://travis-ci.org)
* Isolate app in Docker container
* Include instructions for running containerized app on heroku, AWS, Azure and GCP
* Add spider to parse port data
