
# company_reader_ean_code
## Table of contents
* [General info](#general-info)
* [Description](#description)
* [Setup](#setup)

## General info
There are 3 py file:
* company_db: This file contains functions on database
* company_main: This file is main file
* create_barcode: This file creates barcode

## Description
This project is simple read barcode and generator barcode in company.
You can:
* read workers use (ean code and) web camera
* Add new worker to database and create code (ean)
* check how many people works now
* check all database
* search

Instruction:
We have database with 10 rows (10 workers). You scan barcode using own web camera. When worker go home you scan again and check how many many he/she earned.

## Setup
To run this project, install it use this:

```
$ pip install -r requirements.txt
```
And run:
```
$ py company_main.py
```
If you want own database delete file: db/company.db and first run company_main.py

