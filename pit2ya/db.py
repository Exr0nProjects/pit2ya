from toggl_wrap import get_timers

def get_data():
    global seen
    from csv import reader as csv_reader
    from os import getenv, path
    filepath = getenv('PIT2YA_DIRPATH') or getenv('XDG_DATA_HOME') + '/pit2ya/timers.csv'

    if path.isfile(filepath):
        print("file found!")
        with open(filepath, 'r', newline='') as rf:
            for row in enumerate(csv_reader(rf)): # TODO: convert to dict reader sometime? is it faster?
                yield { 'desc': row[0], 'pid': int(row[1]) }
    else:
        from os import mkdir
        if not path.isdir(filepath[:filepath.rfind('/')]):
            mkdir(filepath[:filepath.rfind('/')])
        print('cached data file not found... loading past toggl data')
        with open(filepath, 'w+', newline='') as wof:
            from csv import writer as csv_writer
            wf = csv_writer(wof)
            for timer in get_timers(3):
                wf.writerow((timer['desc'], timer['pid']))
                yield timer

async def set_data(timers, recent):
    pass
