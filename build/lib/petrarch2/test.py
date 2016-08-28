 
from EventCoder import EventCoder

coder = EventCoder(petrGlobal={}) 

another_coder = EventCoder(petrGlobal=coder.get_PETRGlobals())
 
input_file = open('test_article_173_2.json')
 
content = input_file.read()
 
print content
 
print '==================='
 
print another_coder.encode(content)['nytasiapacific20160622.0002']['sents'][1]['events']
    

 