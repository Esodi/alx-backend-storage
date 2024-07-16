#!/usr/bin/env python3
''' insert documents to a collection '''

def insert_school(mongo_collection, **kwargs):
    ''' function itself '''
    for k, v in kwargs.items():
        res = mongo_collection.insert({k: v})
    return res
