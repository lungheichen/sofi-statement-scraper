# sofi-statement-scraper
Scrapes transaction data from SoFi statements with tabula-py (Pthon 3).

## How to use
*This still needs additional testing.*

First, create a `statements` folder and place all statement .pdfs in there.  
Make sure you have dependencies tabula-py, pandas, and jpype1, and have 
installed Java 8+ and Python 3.8+ per 
https://tabula-py.readthedocs.io/en/latest/:

`pip install tabula-py` 

`pip install pandas`

`pip install jpype1`

then run the following command:

`python sofi-statement-scraper.py`

A .csv file named `SoFi_statements.csv` should be outputted to the root folder 
with all statements data there! 

## Why was this built?
I made this because, as of Feb 2024, SoFi doesn't export statement data in text 
format beyond 2 years.  There are also no easy-to-use respositories that scrape 
SoFi statement data.  This was my attempt at doing so.

