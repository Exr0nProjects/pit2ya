import asyncio
from api import user_start, user_modify
from db import get_data

def entry_start():
#    asyncio.run(user_start())
    user_start()

def entry_modify():
#    asyncio.run(user_modify())
    user_modify()

if __name__ == '__main__':
    # entry_start()
    # entry_modify()
    gen = get_data()
    for i,e in enumerate(gen):
        print(e)
        if i > 10:
            break
    for i,e in enumerate(gen):
        print(i, e)

