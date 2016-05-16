from redis import Redis
from rq import Queue
from test import analysis
from test import write_file


result = {}
q = Queue(connection=Redis())

with open("ip") as file_:
    for line in file_:
        result[line] = 0
        job = q.enqueue(analysis, line, result)
        print result[line]
        job2 = q.enqueue(write_file, result)
        #print job.result
