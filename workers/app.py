import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import redis
from rq import Queue

from nod import main as wrapper_na

r = redis.Redis(host='redis', port=6379, decode_responses=True)
q = Queue('email_queue',connection=r)

def main():
    result = 'test'
    job = q.enqueue(wrapper_na )

    return


if __name__ == "__main__":
    i = 0
    while True:
        try:
            main()
            i = i+1
            if i == 1000:
                break
        except Exception as e:
            print(e)
            pass