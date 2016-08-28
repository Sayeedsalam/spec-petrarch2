import sys

from pyspark import SparkContext, SparkConf
from petrarch2 import EventCoder
#from CameoEventCoder import CameoEventCoder 

def map_articles(articleText):
    return articleText.encode('utf-8')
    

def code_articles(articleText):
     
    coder = EventCoder()
    #print articleText.encode('utf-8')
    events_map = coder.encode(articleText)
    #print events_map
    return str(events_map)

if __name__ == "__main__":
    
  # create Spark context with Spark configuration
    conf = SparkConf().setAppName("Spark Petrarch2")
    sc = SparkContext(conf=conf)
    
    lines = ['{ "type" : "story", "doc_id" : "nytasiapacific20160622.0002", "head_line" : "Lightning Ridge Journal: An Amateur Undertaking in Australian Mining Town With No Funeral Home", "date_line" : "Tue, 21 Jun 2016 03:52:15 GMT", "sentences" : {"array":[ { "sentence_id" : 1, "sentence" : "A Tunisian court has jailed a Nigerian student for two years for helping young militants join an armed Islamic group in Lebanon, his lawyer said Wednesday.", "parse_sentence" : "(ROOT (S (S (NP (DT A) (NNP Tunisian) (NN court)) (VP (VBZ has) (VP (VBN jailed) (NP (DT a) (NNP Nigerian) (NN student)) (PP (IN for) (NP (NP (CD two) (NNS years)) (PP (IN for) (S (VP (VBG helping) (S (NP (JJ young) (NNS militants)) (VP (VB join) (NP (DT an) (JJ armed) (JJ Islamic) (NN group)) (PP (IN in) (NP (NNP Lebanon))))))))))))) (, ,) (NP (PRP$ his) (NN lawyer)) (VP (VBD said) (NP (NNP Wednesday))) (. .)))" } ]}, "corref" : "" }']
        
    linesRDD = sc.parallelize(lines)
 
    events_rdd = linesRDD.map(map_articles)
    events_rdd.pprint(1)
    events_rdd = events_rdd.map(code_articles)
    events_rdd.pprint(1)
    
    events_rdd.saveAsTextFiles("hdfs://dmlhdpc10:9000/Events_SPEC", "OUT")

  
  
