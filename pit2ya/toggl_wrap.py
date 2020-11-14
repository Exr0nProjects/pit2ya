def begin_timer_raw(desc, pid):
    from toggl.api import TimeEntry
    from pendulum import now
    if pid >= 0:
        TimeEntry.start_and_save(start=now(), description=desc, pid=pid).save()
    else:
        TimeEntry.start_and_save(start=now(), pid=pid).save()

def get_timers(days):
    from toggl.api import TimeEntry
    from pendulum import now
    entries = TimeEntry.objects.all_from_reports(start=now().subtract(days=days), stop=now())
    seen = set()
    timers = {}
    for i,e in enumerate(entries):
        if e.description not in seen:
            seen.add(e.description)
            timers[e.description] = { 'pid': int(e.pid or -1) }
        if i % 10 == 0:
            print(f'processed {i} entries', end='\r')
    print("finished processing time entries!")
    return seen, timers

