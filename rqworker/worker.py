from redis import Redis
from rq import Queue
from test import analysis
from test import write_file
import datetime

result_ = {}
q = Queue(connection=Redis(), async = False)
print datetime.datetime.now()
target = open("netname.txt", 'w')
with open("/opt/ip") as file_:
    for line in file_:
        job = q.enqueue(analysis, line, result_)
        job2 = q.enqueue(write_file, result_[line], target)
target.close()
print datetime.datetime.now()