from CameoEventCoder import CameoEventCoder
from datetime import datetime

event_encoder = CameoEventCoder()

input_file = open('test_article_173_2.json')

content = input_file.read()

print content

print '==================='

print event_encoder.encode(content)
    

 