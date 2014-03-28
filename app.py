import logging
import json
import os
from flask import request, url_for
import requests
import sys

def hello():
    print "test"    
    resp = requests.get('http://127.0.0.1:9010/display')
    resp_data = resp.json()
    
    print resp_data['name']
    
    data = {'is_valid':False}
    return json.dumps(data)


