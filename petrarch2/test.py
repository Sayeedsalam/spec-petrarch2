 
from petrarch2 import EventCoder

coder = EventCoder() 
 
input_file = open('test_article_173_2.json')
 
content = input_file.read()
 
print content
 
print '==================='
 
print coder.encode(content)['nytasiapacific20160622.0002']['sents'][1]['events']
    

 