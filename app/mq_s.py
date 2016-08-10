#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 重新设置编码
import sys
import logging as log
from kafka import KafkaProducer

# 编码处理
reload(sys)
sys.setdefaultencoding('utf8')

# 日志配置
log.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='/oalog/oa.log',
                filemode='w')


class Mq_s(object):
    def __init__(self, serverlist, msg):
        self.serverlist = serverlist;
        self.msg = msg

    def producer_msg(self):
        try:
            producer = KafkaProducer(bootstrap_servers=[self.serverlist])
            producer.send('oa_qian', (self.msg).encode("utf-8"))
            producer.flush()
            producer.close(timeout=60)
            return "success"
        except Exception as e:
            logging.error(e)
            return "error"

# if __name__ == '__main__':
# test code
# mq_s = Mq_s('kafka.sunqb.com:9092', 'sunqingbiao;sun;890897;1')
# mq_s.producer_msg()
