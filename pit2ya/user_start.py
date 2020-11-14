import asyncio
from dataclasses import dataclass

# @dataclass(order=True)
# class PrioritizedTimer:
#     from dataclasses import field
#     priority: int
#     description: str=field(compare=False)

# this doesn't work.. no way of updating priorities
# from queue import PriorityQueue
# from random import randint
# class PrioritizedTimer(object):
#     def __init__(self, description: str, priority: int):
#         self.desc = description
#         self.priority = priority
#     def __lt__(self, other):
#         return self.priority > other.priority
#     def __repr__(self):
#         return f'PriTim({self.desc}, {self.priority})'
#
# if __name__ == '__main__':
#     pq = PriorityQueue()
#     for i in range(10):
#         r = randint(1, 1000)
#         print('inserting', r)
#         pq.put(PrioritizedTimer('hi ' + str(r), r))
#     for i in range(10):
#         print(pq.get())

# async def get_data():
#     from pickle import dump, load
#     from toggl.api import TimeEntry
#     from pendulum import now
#     from os import getenv, path
#     filepath = getenv('PIT2YA_DIRPATH') or getenv('XDG_DATA_HOME') + '/pit2ya/timers.pykle'
#     timers = {}
#     if path.isfile(filepath):
#         with open(filepath, 'rb') as rf:
#             timers = load(rf)
#     else:
#         print("Pit2ya data not found... please try again after data has been processed")
#         # from os import mkdir
#         # print('config file not found... loading past month of toggl data')
#         # entries = TimeEntry.objects.all_from_reports(start=now().subtract(months=1), stop=now())
#         # print('    processing time entries...')
#         # if not path.isdir(filepath[:filepath.rfind('/')]):
#         #     mkdir(filepath[:filepath.rfind('/')])
#         # seen = set()
#         # for i,e in enumerate(entries):
#         #     if e.description not in seen:
#         #         seen.add(e.description)
#         #         timers[e.description] = { 'pid': int(e.pid or -1) }
#         #         # writer.writerow((e.description, e.pid or -1))
#         #     if i % 10 == 0:
#         #         print(f'processed {i} entries', end='\r')
#         # with open(filepath, 'wb') as wf:
#         #     dump(timers, wf)
#     return timers


if __name__ == '__main__':
    entry_start()

