# Copyright 2017 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from google.cloud import datastore
from google.cloud import firestore
import datetime
import sys
from datetime import timedelta  
from forecast import Forecast
from settings import PROJECT_ID
from settings import FILE_NAME
from settings import COLLECTION_NAME

db = firestore.Client(PROJECT_ID)

#deletes the entire collection
def delete_collection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).stream()
    deleted = 0

    for doc in docs:
        doc.reference.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)


#list post codes
def list_all_post_codes():
    docs = db.collection(COLLECTION_NAME).stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

#finds a specific postcode
def find_postcode(postcode):
    return db.collection(COLLECTION_NAME).document(postcode).get().to_dict()

#updates an existing entry
def update_locality(postcode, locality, date, min,max):
    collection = db.collection(COLLECTION_NAME)
    document = collection.document(postcode)
    var = Forecast.from_dict(document.get().to_dict())
    var.add_locality(locality, date, min,max )
    document.update(var.to_dict())

#processes a new line from the file 
def add_new_forecast(postcode, locality, date, min,max):
    collection = db.collection(COLLECTION_NAME)
    res = find_postcode(postcode)
    print (res)
    if res is None:
        collection.document(postcode).set(Forecast([postcode, locality, date, min,max,]).to_dict())
    else:
        update_locality(postcode, locality, date, min,max)
        

def main():
    # Simulation for the cloud function
    # Remove all documents within the collection
    delete_collection(db.collection(COLLECTION_NAME), 10)

    # Open the file
    f = open(FILE_NAME, 'r')
    for x in f:
        content = x[0:-1]
        result = content.split('|')
        add_new_forecast(result[2], result[0], result[3], result[5], result[4])


if __name__ == "__main__":
    main()

