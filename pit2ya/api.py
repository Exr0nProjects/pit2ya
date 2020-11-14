import asyncio
from db import get_data, set_data
from toggl_wrap import begin_timer_raw

async def user_start():
    from iterfzf import iterfzf
    timers = await get_data()
    query, desc = iterfzf(timers.keys(), print_query=True, extended=True)

    if desc:
        begin_timer_raw(desc, timers[desc]['pid'])
    else:
        pass    # TODO: collect project information, allow creating new time entries
        # project = input(f"Creating new time entry '{query}'... what project? ")
async def user_modify():
    from iterfzf import iterfzf
    timers = await get_data()
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
