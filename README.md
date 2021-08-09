# firestore_example

This repo is a simple example of how to ingest data to firestore.

## Purpose

Python based example that leverages weather information to store it into the database. 

## Prerequisites

To run the commands described in this document, you need to have followed this guide: 

- Quickstart using a server client library (https://cloud.google.com/firestore/docs/quickstart-servers)

## Running the sample

Change your settings to your project and input info in the settings.py file.
```
PROJECT_ID = '<Your Project>'
COLLECTION_NAME = u'<Your Collection Name>'
FILE_NAME = '<input file>'
```

Install required libraries
```
pip3 install -r requirements.txt
```


Run it with your simple file
```
python3 forecast_loader
```

