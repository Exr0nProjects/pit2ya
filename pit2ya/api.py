import asyncio
from db import get_data, set_data
from toggl_wrap import begin_timer_raw

def user_start():
    from iterfzf import iterfzf
    desc_list = get_data()
    query, desc = iterfzf(desc_list, print_query=True, extended=True)
    if desc:
        begin_timer_raw(desc, desc_list.timers[desc]['pid'])
    else:
        pass    # TODO: collect project information, allow creating new time entries

def user_modify():
    from iterfzf import iterfzf
    desc_list = get_data()
    query, desc = iterfzf(desc_list, print_query=True, extended=True)
    from toggl.api import TimeEntry
    cur = TimeEntry.objects.current()
    if cur is None:
        print('No current running timer!')
        begin_timer_raw(desc, desc_list.timers[desc]['pid'])
        set_data(desc_list.timers, desc)
    elif desc:
        setattr(cur, 'description', desc)
        setattr(cur, 'project', desc_list.timers[desc]['pid'])
        cur.save()
    else:       # create a whole new timer
        desc = query
        setattr(cur, 'description', desc)
        setattr(cur, 'project', desc_list.timers[desc]['pid'])
        cur.save()
    set_data(desc_list.timers, desc)


