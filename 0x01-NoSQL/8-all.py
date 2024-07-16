#!/usr/bin/env python3
''' lists all documents in a collection '''

def list_all(mongo_collection):
    ''' function itself '''
    docs = list(mongo_collection.find())
    return docs if docs else []
