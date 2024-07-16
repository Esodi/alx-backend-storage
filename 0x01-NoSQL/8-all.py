#!/usr/bin/env python3
''' lists all documents in a collection '''

if __name__ == "__main__":
    def list_all(mongo_collection):
        ''' function itself '''
        if not mongo_collection:
            return []

        return list(mongo_collection.find())
