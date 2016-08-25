import sys

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
#from CameoEventCoder import CameoEventCoder 

def code_articles(articleText):
    from CameoEventCoder import CameoEventCoder 
    coder = CameoEventCoder()
    events_map = coder.encode(articleText)
    return str(events_map)

if __name__ == "__main__":

  # create Spark context with Spark configuration
    conf = SparkConf().setAppName("Spark Count")
    sc = SparkContext(conf=conf)
    ssc = StreamingContext(sc, 120)
    kafkaStream = KafkaUtils.createStream(ssc=ssc,
                                        zkQuorum='dmlhdpc1',
                                        groupId='dmlhdpc1',
                                        topics={'petrarch':1})
  
 
    lines = kafkaStream.map(lambda x: x[1])
    events_rdd = lines.map(code_articles)
    
    events_rdd.saveAsTextFiles("TEST", "OUT")

    ssc.start()
    ssc.awaitTermination()
  
  
