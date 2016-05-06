from redis import Redis
from rq import Queue
from netname import analysis


q = Queue(connection=Redis())

result = q.enqueue(analysis, '/opt/ip')
