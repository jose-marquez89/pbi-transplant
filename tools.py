import os
import json
import sys

def transplant_bookmarks(source, target):
    """Copy over bookmarks"""        
    source_config = json.loads(source['config'])
    target_config = json.loads(target['config'])

    source_bookmarks = source_config['bookmarks']
    target_config['bookmarks'] = source_bookmarks

    target['config'] = json.dumps(target_config)

    return target

# TODO: Zip functionality


if __name__ == "__main__":
    with open(source, 'rb') as s:
        source_json = json.load(s)

    with open(target, 'rb') as t:
        target_json = json.load(s)

    output = transplant_bookmarks(source_json, target_json)

    with open("CopiedLayouy", "wb") as f:
        json.dump(output, f)