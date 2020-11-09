
def get_data():
    from os import getenv, path
    from sys import argv

    filepath=None
    if len(argv) > 1:
        filepath = argv[1]
    else:
        filepath = getenv('XDG_DATA_HOME') + '/pit2ya/timers.csv'

    print('looking for timers at', filepath)
    timers = {}
    if not path.isfile(filepath):
        from csv import writer as csv_writer
        from toggl.api import TimeEntry
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

def begin_timer():
    from iterfzf import iterfzf
    query, desc = iterfzf(get_data().keys(), print_query=True)

    from toggl import api
    if desc:
        pass

if __name__ == '__main__':
    # print(get_data())
    begin_timer()

