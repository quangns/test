import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import netname
from rq import Queue, Worker, Connection


with Connection():
    qs = map(Queue, sys.argv[1:]) or [Queue('default')]
    w = Worker(qs, default_result_ttl=0)
    w.work()
