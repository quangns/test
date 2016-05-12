from redis import Redis
from rq import Queue
from netname import write_file


q = Queue(connection=Redis())
job = q.enqueue(write_file)

