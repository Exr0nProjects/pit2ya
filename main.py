
def get_data():
    from os import getenv, path
    from sys import argv

    filepath=None
    if len(argv) > 1:
        filepath = argv[1]
    else:
        filepath = getenv('XDG_DATA_HOME') + '/pit2ya/timers.csv'

    timers = {}
    if not path.isfile(filepath):
        from csv import writer as csv_writer
        from toggl.api import TimeEntry
        from pendulum import now
        print('config file not found... loading past month of toggl data')
        entries = TimeEntry.objects.all_from_reports(start=now().subtract(months=1), stop=now())
        print('    processing time entries...')
        with open(filepath, 'w+', newline='') as wf:
            writer = csv_writer(wf)
            seen = set()
            for i,e in enumerate(entries):
                if e.description not in seen:
                    seen.add(e.description)
                    timers[e.description] = { 'pid': e.pid }
                    writer.writerow((e.description, e.pid or -1))
                if i % 10 == 0:
                    print(f'processed {i} entries', end='\r')
    else:
        # when csv.reader is the fastest
        with open(filepath, 'r', newline='') as rf:
            from csv import reader
            rd = reader(rf)
            for row in rd:
                timers[row[0]] = row[1]

    return timers

def begin_timer(desc, pid):
    from toggl.api import TimeEntry
    from pendulum import now
    entry = TimeEntry.start_and_save(start=now(), description=desc, pid=pid)
    entry.save()

def handle():
    from iterfzf import iterfzf
    timers = get_data()
    query, desc = iterfzf(timers.keys(), print_query=True)

    if desc:
        begin_timer(desc, timers[desc])
    else:
        pass    # TODO: collect project information, allow creating new time entries
        # project = input(f"Creating new time entry '{query}'... what project? ")

if __name__ == '__main__':
    handle()

