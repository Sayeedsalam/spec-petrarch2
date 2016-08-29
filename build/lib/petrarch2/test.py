  
from EventCoder import EventCoder
 
coder = EventCoder(petrGlobal={}) 
 
another_coder = EventCoder(petrGlobal=coder.get_PETRGlobals())
  
input_file = open('test_article_0353.json')
  
content = input_file.read()
  
print content
  
print '==================='
  
print another_coder.encode(content)

# from dateutil import parser
# from datetime import datetime
# 
# dateObject = parser.parse("")
# 
# article_date = datetime.strftime(dateObject, '%Y%m%d') 
# 
# 
# print article_date 