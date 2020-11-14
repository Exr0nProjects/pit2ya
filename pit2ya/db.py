seen = set()

from toggl_wrap import get_timers

async def get_data():
    global seen
    from csv import reader as csv_reader
    # from pickle import dump, load
    from os import getenv, path
    filepath = getenv('PIT2YA_DIRPATH') or getenv('XDG_DATA_HOME') + '/pit2ya/timers.pykle'
    timers = {}
    if path.isfile(filepath):
        with open(filepath, 'rb') as rf:
            for row in csv_reader(rf):
                yield
            return (row[0]: { 'pid': int(row[1] or -1) } for row in rd)
            # timers = load(rf)
    else:
        from os import mkdir
        if not path.isdir(filepath[:filepath.rfind('/')]):
            mkdir(filepath[:filepath.rfind('/')])
        print('config file not found... loading past month of toggl data')
        seen, timers = get_timers(30)
        with open(filepath, 'wb') as wf:
            dump(timers, wf)
    return timers

async def set_data(timers, recent):
    pass
