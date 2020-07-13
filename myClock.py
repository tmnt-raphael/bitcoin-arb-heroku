from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue
from worker import conn
from utils import count_words_at_url
import time

sched = BlockingScheduler()
q = Queue(connection=conn)

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    job = q.enqueue(count_words_at_url, 'http://heroku.com')

    time.sleep(2)
    print(job.result)

sched.start()