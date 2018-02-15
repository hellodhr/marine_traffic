# marine_traffic
A collection of spiders to crawl data from http://www.marinetraffic.com

## About
Given a list of unique identifiers, retrieve various information from http://www.marinetraffic.com, store it in data structures and write full result to JSON file. Check out the project's [wiki](https://github.com/slangenbach/marine_traffic/wiki) for further information. Open points are managed via [projects](https://github.com/slangenbach/marine_traffic/projects) and [issues](https://github.com/slangenbach/marine_traffic/issues).


## Usage 
Make sure to create an isolated Python 3.x environment (using [virtualenv](https://virtualenv.pypa.io/en/stable/userguide/#usage) or [conda](https://conda.io/docs/user-guide/tasks/manage-environments.html#)) before running the code

### Get source code
```
git clone https://github.com/slangenbach/marine_traffic.git
cd marine_traffic
```
### Create isolated environment 
Using virtualenv:
```
pip install virtualenv
virtualenv <name of your environment>
source activate <name of your environment>/bin/activate
pip install -r requirements.txt
```
or alternatively using conda:
```
conda env create -n <name of your environment>
source activate <name of your environment>
conda env update -f conda_<win/osx depending on your operating system>.yml
```

### Copy input file to target directoy
The crawler automatically reads an input file (CSV) from the top vessel_spider directory
By default, the second column of the file is used to extract vessel identification IDs (IMO) for crawling
```
cd vessel_spider
cp -v <path to your your input file> .
```
### Start crawler
```
scrapy crawl vessel -o <output>.json
```
