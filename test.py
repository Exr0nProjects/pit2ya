from queue import PriorityQueue
from random import randint
class PrioritizedTimer(object):
    def __init__(self, description: str, priority: int):
        self.desc = description
        self.priority = priority
    def __lt__(self, other):
        return self.priority > other.priority
    def __repr__(self):
        return f'PriTim({self.desc}, {self.priority})'

if __name__ == '__main__':
    pq = PriorityQueue()
    for i in range(10):
        r = randint(1, 1000)
        print('inserting', r)
        pq.put(PrioritizedTimer('hi ' + str(r), r))
    for i in range(10):
        print(pq.get())

