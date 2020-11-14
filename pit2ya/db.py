from toggl_wrap import get_timers
from csv import reader as csv_reader
from os import getenv, path

def api_and_yield(path, days, timers):
    with open(path, 'w+', newline='') as wof:
        from csv import writer as csv_writer
        wf = csv_writer(wof)
        for timer in get_timers(days, silent=days>7):
            if not timer['desc'] in timers:
                wf.writerow([timer['desc'], timer['pid']])
                timers[timer['desc']] = { 'pid': timer['pid'] }
                yield timer['desc']

class get_data():   # https://stackoverflow.com/q/34073370
    filepath = getenv('PIT2YA_DIRPATH') or getenv('XDG_DATA_HOME') + '/pit2ya/timers.csv'
    dirpath = filepath[:filepath.rfind('/')]

    def __init__(self):
        self.timers = {}

    def __iter__(self):
        if path.isfile(self.filepath):
            with open(self.filepath, 'r', newline='') as rf:
                for row in enumerate(csv_reader(rf)): # TODO: convert to dict reader sometime? is it faster?
                    # yield { 'desc': row[0], 'pid': int(row[1]) }
                    self.timers[row[1][0]] = { 'pid': int(row[1][1] or -1) }
                    yield row[1][0]
            yield from api_and_yield(self.filepath, 1, self.timers)
        else:
            from os import mkdir
            if not path.isdir(self.dirpath):
                mkdir(self.dirpath)
            print('cached data file not found... loading past toggl data')
            yield from api_and_yield(self.filepath, 3, self.timers)

async def set_data(timers, recent):
    pass

