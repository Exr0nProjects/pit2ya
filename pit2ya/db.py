from toggl_wrap import get_timers
from os import getenv, path, replace
from csv import reader, writer
from itertools import chain

filepath = getenv('PIT2YA_DIRPATH') or getenv('XDG_DATA_HOME') + '/pit2ya/timers.csv'
dirpath = filepath[:filepath.rfind('/')]

def api_and_yield(path, days, timers):
    with open(path, 'w+', newline='') as wof:
        wf = writer(wof)
        for timer in get_timers(days):
            if not timer['desc'] in timers:
                wf.writerow([timer['desc'], timer['pid']])
                timers[timer['desc']] = { 'pid': timer['pid'] }
                yield timer['desc']

class get_data():   # https://stackoverflow.com/q/34073370
    def __init__(self):
        self.timers = {}

    def __iter__(self):
        if path.isfile(filepath):
            with open(filepath, 'r', newline='') as rof:
                for row in enumerate(reader(rof)): # TODO: convert to dict reader sometime? is it faster?
                    # yield { 'desc': row[0], 'pid': int(row[1]) }
                    self.timers[row[1][0]] = { 'pid': int(row[1][1] or -1) }
                    yield row[1][0]
            yield from api_and_yield(filepath, 1, self.timers)
        else:
            from os import mkdir
            if not path.isdir(dirpath):
                mkdir(dirpath)
            print('cached data file not found... loading past toggl data')
            yield from api_and_yield(filepath, 60, self.timers)

def set_data(desc_list, recent):
    print("api requested.. saving data", len(desc_list.timers))
    with open(filepath + '.bak', 'w+', newline='') as wof:    # TODO: delete the line instead of rewriting. or use an actual database
        wf = writer(wof)
        wf.writerow([recent, desc_list.timers[recent]['pid']])
        # for timer_k in chain(desc_list.timers, desc_list):
        for timer_k in desc_list.timers:
            if timer_k is not recent:
                wf.writerow([timer_k, desc_list.timers[timer_k]['pid']])
        # print('finished saving cached.. consuming iter')
        # count = 0
        # for timer_k in desc_list:   # TODO: doesn't consume remaining... it appears to just replay the previous?
        #     print('    ', timer_k)
        #     if timer_k is not recent:
        #         wf.writerow([timer_k, desc_list.timers[timer_k]['pid']])
        #         count += 1
        # print('got another', count, 'timers')
        replace(filepath + '.bak', filepath)

