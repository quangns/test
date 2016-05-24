from redis import Redis
from rq import Queue
from netname import main_


q = Queue(connection=Redis())
q.empty()
with open("ip") as file_:
    for line in file_:
        job = q.enqueue(main_, line)
