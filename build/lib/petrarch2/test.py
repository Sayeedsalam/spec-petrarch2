from CameoEventCoder import CameoEventCoder
from datetime import datetime
import json

event_encoder = CameoEventCoder()

input_file = open('test_article_173_2.json')

content = input_file.read()

print content

print '==================='

print event_encoder.encode(content)['nytasiapacific20160622.0002']['sents'][1]['events']
    

 