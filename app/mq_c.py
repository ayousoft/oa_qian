#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 重新设置编码
import sys
import logging as log
from kafka import KafkaConsumer
from attendance import Attendance

reload(sys)
sys.setdefaultencoding('utf8')


# log.basicConfig(level=log.DEBUG)

def consumer_msg(serverlist):
    consumer = KafkaConsumer('oa_qian',
                             group_id='my-group',
                             bootstrap_servers=[serverlist])
    for message in consumer:
        msg = bytes.decode(message.value)
        msglist = msg.split(";")
        username = msglist[0]
        password = msglist[1]
        key = msglist[2]
        type = msglist[3]
        oa = Attendance(username, password, key)
        if (type == '1'):
            print oa.singin()
        else:
            print oa.singout()


if __name__ == '__main__':
    consumer_msg('kafka.sunqb.com:9092')
