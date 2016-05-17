from redis import Redis
from rq import Queue
from netname import analysis


q = Queue(connection=Redis())
with open("ip") as file_:
    for line in file_:
        job = q.enqueue(analysis, line)
