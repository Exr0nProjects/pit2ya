import asyncio
from pit2ya.api import user_start, user_modify

def entry_start():
    return user_start()

def entry_modify():
    return user_modify()

def get_current():
    from toggl.api import TimeEntry
    print(TimeEntry.objects.current().description)

