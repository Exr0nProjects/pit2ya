# def get_data():
#     from os import getenv, path
#     from sys import argv
#
#     filepath=None
#     # if len(argv) > 1:
#     #     filepath = argv[1]
#     # else:
#     filepath = getenv('XDG_DATA_HOME') + '/pit2ya/timers.csv'
#
#     timers = {}
#     if not path.isfile(filepath):
#         from csv import writer as csv_writer
#         from toggl.api import TimeEntry
#         from pendulum import now
#         from os import mkdir
#         print('config file not found... loading past month of toggl data')
#         entries = TimeEntry.objects.all_from_reports(start=now().subtract(months=1), stop=now())
#         print('    processing time entries...')
#         mkdir(filepath[:filepath.rfind('/')])
#         with open(filepath, 'w+', newline='') as wf:
#             writer = csv_writer(wf)
#             seen = set()
#             for i,e in enumerate(entries):
#                 if e.description not in seen:
#                     seen.add(e.description)
#                     timers[e.description] = { 'pid': int(e.pid) }
#                     writer.writerow((e.description, e.pid or -1))
#                 if i % 10 == 0:
#                     print(f'processed {i} entries', end='\r')
#     else:
#         # when csv.reader is the fastest
#         with open(filepath, 'r', newline='') as rf:
#             from csv import reader
#             rd = reader(rf)
#             for row in rd:
#                 timers[row[0]] = { 'pid': int(row[1]) }
#
#     return timers

def get_data():
    from pickle import dump, load
    from os import getenv, path
    filepath = getenv('PIT2YA_DIRPATH') or getenv('XDG_DATA_HOME') + '/pit2ya/timers.csv'
    data = None
    if path.isfile(filepath):
        with open(filepath, 'rb') as rf:
            data = load(rf)
            print(data)
    else:
        timers = {}
        from csv import writer as csv_writer
        from toggl.api import TimeEntry
        from pendulum import now
        from os import mkdir
        print('config file not found... loading past month of toggl data')
        entries = TimeEntry.objects.all_from_reports(start=now().subtract(months=1), stop=now())
        print('    processing time entries...')
        if not path.isdir(filepath[:filepath.rfind('/')]):
            mkdir(filepath[:filepath.rfind('/')])
        seen = set()
        for i,e in enumerate(entries):
            if e.description not in seen:
                seen.add(e.description)
                timers[e.description] = { 'pid': int(e.pid or -1) }
                # writer.writerow((e.description, e.pid or -1))
            if i % 10 == 0:
                print(f'processed {i} entries', end='\r')
        with open(filepath, 'wb') as wf:
            dump(timers, wf)
    return timers

def begin_timer_raw(desc, pid):
    from toggl.api import TimeEntry
    from pendulum import now
    if pid >= 0:
        TimeEntry.start_and_save(start=now(), description=desc, pid=pid).save()
    else:
        TimeEntry.start_and_save(start=now(), pid=pid).save()

def user_start():
    from iterfzf import iterfzf
    timers = get_data()
    query, desc = iterfzf(timers.keys(), print_query=True, extended=True)

    if desc:
        begin_timer_raw(desc, timers[desc]['pid'])
    else:
        pass    # TODO: collect project information, allow creating new time entries
        # project = input(f"Creating new time entry '{query}'... what project? ")
def user_modify():
    from iterfzf import iterfzf
    timers = get_data()
    query, desc = iterfzf(timers.keys(), print_query=True, extended=True)

    from toggl.api import TimeEntry

    cur = TimeEntry.objects.current()
    if cur is None:
        print('No current running timer!')
        begin_timer_raw(desc, timers[desc]['pid'])
    elif desc:
        setattr(cur, 'description', desc)
        setattr(cur, 'project', timers[desc]['pid'])
        cur.save()

if __name__ == '__main__':
    get_data()

