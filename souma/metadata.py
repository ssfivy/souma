#!/usr/bin/env python3

# Generates dumpfile metadata

import json
import os
import time

METADATA_FILENAME = 'metadata.json'

def gen_metadata_v1_str():
    metadata = {}
    metadata['fileversion'] = 1
    metadata['creationtime'] = time.time()
    return json.dumps(metadata, indent=1, sort_keys=True)

def gen_metadata_v1_file(directory):
    with open(os.path.join(directory, METADATA_FILENAME), 'w', encoding='utf-8') as fd:
        fd.write(gen_metadata_v1_str())
