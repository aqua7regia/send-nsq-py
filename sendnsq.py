import nsq
import tornado.ioloop
import time
import json

def pub_message():
    msg = json.dumps({
        "field1": "value",
        "field2": "value"
    })
    writer.pub('topic', msg, finish_pub)

def finish_pub(conn, data):
    print data

writer = nsq.Writer(nsqd_tcp_addresses=['127.0.0.1:4150'])
writer.name = 'abc'
tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
nsq.run()
