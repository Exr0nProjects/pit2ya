import asyncio
from api import user_start, user_modify

from db import get_data, set_data

def entry_start():
#    asyncio.run(user_start())
    user_start()

def entry_modify():
#    asyncio.run(user_modify())
    user_modify()

if __name__ == '__main__':
    # entry_start()
    entry_modify()
