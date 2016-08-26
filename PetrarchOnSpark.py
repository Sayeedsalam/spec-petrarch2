import sys

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
#from CameoEventCoder import CameoEventCoder 

def code_articles(articleText):
    import CameoEventCoder 
    coder = CameoEventCoder()
    events_map = coder.encode(articleText)
    print events_map
    return str(events_map)

if __name__ == "__main__":

  # create Spark context with Spark configuration
    conf = SparkConf().setAppName("Spark Petrarch2")
    sc = SparkContext(conf=conf)
    sc.addPyFile("petrarch_shipped.zip")
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
  
  
